from pyramid.view import view_config

# Servicios
from .. api.sitios import RepositorioSitio

@view_config(route_name='get_sitios',
             renderer='json')
def get_sitios_api(request):
    sitios = RepositorioSitio.all_sitios(request)
    return sitios

@view_config(route_name='get_sitio',
             renderer='json')
def get_sitio_api(request):
    id_sitio = request.matchdict['id_sitio']
    sitio = RepositorioSitio.get_sitio(request, id_sitio)
    return sitio