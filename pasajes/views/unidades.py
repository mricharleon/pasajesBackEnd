from pyramid.view import view_config

# Servicios
from .. api.unidades import RepositorioUnidad

@view_config(route_name='get_unidades',
             renderer='json',
             permission='view')
def get_unidades_api(request):
    
    user = request.user
    id_usuario = request.user.id
    if user.grupo.nombre == 'Administrador':
        unidades = RepositorioUnidad.all_unidades(request)
    else:
        unidades = RepositorioUnidad.all_unidades_usuario(request, id_usuario)

    return unidades

@view_config(route_name='get_unidad',
             renderer='json')
def get_unidad_api(request):

    id_unidad = request.matchdict['id_unidad']
    unidad = RepositorioUnidad.get_unidad(request, id_unidad)
    
    return unidad