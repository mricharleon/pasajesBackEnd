from pyramid.view import view_config

# Servicios
from .. api.clases import RepositorioClase

@view_config(route_name='get_clases',
             renderer='json')
def clases_api(request):
    clases = RepositorioClase.all_clases(request)
    return clases