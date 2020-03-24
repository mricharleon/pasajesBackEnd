from pyramid.view import view_config

# Servicios
from .. api.roles import RepositorioRol

@view_config(route_name='get_roles',
             renderer='json')
def roles_api(request):
    roles = RepositorioRol.all_roles(request)
    return roles