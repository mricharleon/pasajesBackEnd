from pyramid.view import view_config

# Servicios
from .. api.usuarios import RepositorioUsario

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
