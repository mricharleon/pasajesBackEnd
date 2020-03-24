from pyramid.view import view_config

# Servicios
from .. api.pasajes import RepositorioPasaje

@view_config(route_name='get_pasajes',
             renderer='json')
def get_pasajes_api(request):
    fecha = request.matchdict['fecha']
    origen = request.matchdict['origen']
    destino = request.matchdict['destino']
    pasajes = RepositorioPasaje.all_pasajes(request, fecha, origen, destino)
    return pasajes

@view_config(route_name='get_pasaje',
             renderer='json')
def get_pasaje_api(request):
    id_pasaje = request.matchdict['id_pasaje']
    pasaje = RepositorioPasaje.get_pasaje(request, id_pasaje)
    return pasaje