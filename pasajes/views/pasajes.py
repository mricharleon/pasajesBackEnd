from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

# Modelos
from .. import models

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
    data = request.json_body
    pasaje = RepositorioPasaje.get_pasaje(request, data['id'])

    pasaje.salida = data.get('salida')
    pasaje.llegada = data.get('llegada')
    pasaje.precio = data.get('precio')
    pasaje.asientos_disponibles = data.get('asientos_disponibles')
    pasaje.origen_sitio_id = data.get('origen').get('id')
    pasaje.destino_sitio_id = data.get('destino').get('id')
    pasaje.unidad_id = data.get('unidad').get('id')

    if request.dbsession.add(pasaje) == None:
        response = {
            'msg': 'Pasaje editado correctamente!',
            'status': '200',
        }
    else:
        response = {
            'msg': 'Error, Pasaje no guardado!',
            'status': '422',
        }

    return response