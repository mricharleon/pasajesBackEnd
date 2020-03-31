from pyramid.view import view_config

# Servicios
from .. api.usuarios import RepositorioUsario

@view_config(route_name='api_usuario',
             renderer='json')
def get_sitio_api(request):
    id_usuario = request.matchdict['id_usuario']
    usuario = RepositorioUsario.get_usuario(request, id_usuario)
    return usuario