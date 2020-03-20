from pyramid.view import view_config

# Servicios
from .. api.pasajes import RepositorioPasaje

@view_config(route_name='get_pasajes',
             renderer='json',
             permission='view')
def view_api(request):
    paginas = RepositorioPasaje.all_pasajes(request)
    return paginas