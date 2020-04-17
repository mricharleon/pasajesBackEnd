from pyramid.view import view_config

# Servicios
from .. api.unidades import RepositorioUnidad

@view_config(route_name='get_unidades',
             renderer='json')
def get_unidades_api(request):
    unidades = RepositorioUnidad.all_unidades(request)
    return unidades

@view_config(route_name='get_unidad',
             renderer='json')
def get_unidad_api(request):
    id_unidad = request.matchdict['id_unidad']
    unidad = RepositorioUnidad.get_unidad(request, id_unidad)
    return unidad