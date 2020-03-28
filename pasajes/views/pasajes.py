from pyramid.view import view_config

# Servicios
from .. api.pasajes import RepositorioPasaje


# Obtiene todos los pasajes ecistentes
@view_config(route_name='get_all_pasajes',
             renderer='json')
def get_all_pasajes_api(request):
    pasajes = RepositorioPasaje.get_all_pasajes(request)
    return pasajes

# Obtiene todos los pasajes de acuerdo a la fecha, origen y destino
@view_config(route_name='get_pasajes',
             renderer='json')
def get_pasajes_api(request):
    fecha = request.matchdict['fecha']
    origen = request.matchdict['origen']
    destino = request.matchdict['destino']
    pasajes = RepositorioPasaje.all_pasajes(request, fecha, origen, destino)
    return pasajes

# Obtiene un solo pasaje de acuerdo a su Id
@view_config(route_name='get_pasaje',
             renderer='json')
def get_pasaje_api(request):
    id_pasaje = request.matchdict['id_pasaje']
    pasaje = RepositorioPasaje.get_pasaje(request, id_pasaje)
    return pasaje

# Guarda un pasaje Editado
@view_config(route_name='add_edit_pasaje',
             request_method='PUT',
             renderer='json')
def add_edit_pasaje_api(request):
    print(request.json_body)
    return 'Ok'