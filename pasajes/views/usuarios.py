from pyramid.view import view_config
from pyramid.response import Response

from pyramid.security import remember

from .. import constants as enum
from ..viewmodels.create_usuario_viewmodel import CreateUsuarioViewModel

# Servicios
from .. api.usuarios import RepositorioUsario
from .. api.grupos import RepositorioGrupo

@view_config(route_name='api_usuario',
             renderer='json')
def get_sitio_api(request):
    id_usuario = request.matchdict['id_usuario']
    usuario = RepositorioUsario.get_usuario(request, id_usuario)
    return usuario


@view_config(route_name='api_check_username',
             renderer='json')
def api_check_username(request):
    """Verifica que no se repita el username
    """
    username = request.matchdict['username']
    check_username = RepositorioUsario.check_username(request, username)

    return check_username


@view_config(route_name='api_check_email',
             renderer='json')
def api_check_email(request):
    """Verifica que no este repetido el email
    """
    email = request.matchdict['email']
    check_email = RepositorioUsario.check_email(request, email)

    return check_email


def set_grupo(request, usuario_data):

    if usuario_data.get('grupo'):
        if request.session['user'].grupo.nombre == enum.Usuario.GRUPO_ADMINISTRADOR.value:
            return usuario_data.get('grupo').get('id')
    elif 'user' in request.session:
        grupo_cooperativa = RepositorioGrupo.get_grupo(request,
                                                enum.Usuario.GRUPO_COOPERATIVA.value)
        return grupo_cooperativa.id
    else:
        grupo_cliente = RepositorioGrupo.get_grupo(request,
                                                   enum.Usuario.GRUPO_CLIENTE.value)
        return grupo_cliente.id

@view_config(route_name='usuarios',
             renderer='json',
             request_method='POST')
def api_add_usuario(request):

    try:
        usuario_data = request.json_body
    except Exception as x:
        return Response(status=400, json_body={'titulo': 'Petición errónea!',
                                               'msg': 'No se pudo parsear tu petición POST como un JSON: ' + str(x)})

    vm = CreateUsuarioViewModel(usuario_data)
    vm.compute_details()
    if vm.errors:
        return Response(status=400, json_body=vm.error_msg)

    cod_verificacion = vm.usuario.generar_cod_verificacion()
    pass_temporal = vm.usuario.generar_pass_temporal()

    # Setea atributos automaticos al nuevo usuario
    vm.usuario.set_cod_verificacion(cod_verificacion)
    vm.usuario.set_password(pass_temporal)
    vm.usuario.activo = False
    # Comprueba el tipo de usuario logueado para la asignación de grupo
    vm.usuario.grupo_id = set_grupo(request, usuario_data)

    try:
        usuario = RepositorioUsario.add_usuario(request, vm.usuario)
        email = usuario.enviar_mensaje(request, pass_temporal)
        return Response(status=200, json_body={'titulo': 'Usuario registrado!',
                                               'msg': email.get('msg')})
    except Exception as x:
        return Response(status=500, json_body={'titulo':'Sucedio algo inesperado!',
                                               'msg': 'No se pudo guardar el usuario: ' + str(x)})


@view_config(route_name='api_check_cod_verificacion',
             renderer='json')
def api_check_cod_verificacion(request):
    """Verifica que coincida el codigo de verficacion y procede a activar y loguear la cuenta
    """
    cod_verificacion = request.matchdict['cod_verificacion']
    user = RepositorioUsario.check_cod_verificacion(request, cod_verificacion)
    if user is not None:      
        # cambiar estado del atributo user.activo
        user.set_activo(True)
        user.remove_cod_verificacion()
        # Logueo de usuario
        request.session['user'] = user
        headers = remember(request, user.id)
        response = Response(json_body=user.__json__(request))
        response.headers.extend(headers)
        return response
    else:
        return Response(status=400, json_body={'titulo': 'Usuario no encontrado',
                                               'msg': 'Revisa el código de verificación del enlace'})
