from pyramid.httpexceptions import HTTPFound, HTTPOk
from pyramid.response import Response
from pyramid.security import (
    remember,
    forget,
    )
from pyramid.view import (
    forbidden_view_config,
    view_config,
)

from sqlalchemy import or_

from sqlalchemy.orm import lazyload

from ..models import User, Grupo


@view_config(route_name='api_login', renderer='json')
def api_login(request):

    login_data = request.json_body

    if 'login' in login_data and 'password' in login_data:
        login = login_data.get('login')
        password = login_data.get('password')
        user = request.dbsession.query(User).filter(or_(User.username == login, User.email == login)).first()
        if user is not None and not user.activo:
            return Response(status=403, json_body={'titulo':'Cuenta inactiva',
                                                   'msg':'Revisa tu correo [{}] para activarla'.format(user.email)})
        if user is not None and user.check_password(password):
            # Graba en la session el usuario (se grabará en redis)
            request.session['user'] = user
            headers = remember(request, user.id)
            response = Response( json_body=user.__json__(request) )
            response.headers.extend(headers)
            return response
        
    return Response(status=403, json_body={'titulo': 'Credenciales incorrectas',
                                           'msg': 'Por favor, intenta nuevamente'})


@view_config(route_name='api_logout')
def api_logout(request):
    headers = forget(request)
    response = Response( '' )
    response.headers.extend(headers)
    return response


@view_config(route_name='login', renderer='../templates/login.jinja2')
def login(request):
    next_url = request.params.get('next', request.referrer)
    if not next_url:
        next_url = request.route_url('view_wiki')
    message = ''
    login = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        user = request.dbsession.query(User).filter(or_(User.username==login, User.email==login)).first()
        if user is not None and user.check_password(password):
            headers = remember(request, user.id)
            return HTTPFound(location=next_url, headers=headers)
        message = 'Failed login'

    return dict(
        message=message,
        url=request.route_url('login'),
        next_url=next_url,
        login=login,
        )

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    next_url = request.route_url('view_api')
    return HTTPFound(location=next_url, headers=headers)

# Se dispara cuando la petición no pasa los permissions
@forbidden_view_config()
def forbidden_view(request):
    u = request.session.get('user')
    return Response(status=401, json_body={'msg':'No tienes permisos para realizar eso!',
                                           'error':str(u.grupo.nombre)})
