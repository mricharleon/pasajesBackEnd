from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import (
    Authenticated,
    Everyone,
)
from pyramid.security import (
    remember,
)
from pyramid.response import Response

from sqlalchemy.orm import lazyload

from .models import User, Grupo


class MyAuthenticationPolicy(AuthTktAuthenticationPolicy):
    def authenticated_userid(self, request):
        # user = request.user
        user = get_user(request)
        if user is not None:
            return user.id
    
    def effective_principals(self, request):
        principals = [Everyone]
        # user = request.user
        user = get_user(request)
        if user is not None:
            principals.append(Authenticated)
            principals.append(str(user.id))
            principals.append('grupo:' + user.grupo.nombre)
        return principals

def get_user(request):
    user_id = request.unauthenticated_userid
    if user_id is not None:
        # Controla que si la session (redis) fuese borrada en el cliente,
        # se pueda acceder al usuario desde la base de datos
        try:
            user = request.session['user']
            print('Recuperando data de [{}] desde Redis Session! '.format(
                user.username) )
        except:
            user = request.dbsession.query(User).filter(User.id == user_id).first()
            request.session['user'] = user
            print('Recuperando data de [{}] desde BD! '.format(
                user.username))

        return user

def includeme(config):
    settings = config.get_settings()
    authn_policy = MyAuthenticationPolicy(
        settings['auth.secret'],
        # max_age=settings['auth.max_age'],
        hashalg='sha512',
    )
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_request_method(get_user, 'user', reify=True)
