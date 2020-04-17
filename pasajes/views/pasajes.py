from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from json import loads

from ..viewmodels.update_pasaje_viewmodel import CreatePasajeViewModel, UpdatePasajeViewModel

# Modelos
from .. import models

# Servicios
from .. api.pasajes import RepositorioPasaje


# Obtiene todos los pasajes ecistentes
@view_config(route_name='get_all_pasajes',
             renderer='json',
             permission="edit")
def get_all_pasajes_api(request):

    if request.user.grupo.nombre == 'Cooperativa':
        id_usuario = request.user.id
        pasajes = RepositorioPasaje.get_all_pasajes_cooperativa(request, id_usuario)
    else:
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
    if pasajes:
        return pasajes
    return dict(msg='No hay resultados para tu búsqueda')
    

# Obtiene un solo pasaje de acuerdo a su Id
@view_config(route_name='get_pasaje',
             renderer='json',)
def get_pasaje_api(request):

    id_pasaje = request.matchdict['id_pasaje']
    pasaje = RepositorioPasaje.get_pasaje(request, id_pasaje)
    return pasaje


# Guarda un pasaje Editado
@view_config(route_name='get_pasaje',
             request_method='PUT',
             permission="edit")
def put_pasaje_api(request):
    pasaje_id = request.matchdict.get('id_pasaje')
    pasaje = RepositorioPasaje.get_pasaje(request, pasaje_id)

    if not pasaje:
        msg = "El pasaje con el Id '{}' no fue encontrado.".format(pasaje_id)
        return Response(status=404, json_body={'msg': msg})

    try:
        pasaje_data = request.json_body
    except:
        return Response(status=400, json_body={'msg':'No se puede parsear tu petición a JSON.'})

    vm = UpdatePasajeViewModel(pasaje_data, pasaje_id)
    vm.compute_details()
    if vm.errors:
        return Response(status=400, json_body={'msg':vm.error_msg})

    try:
        RepositorioPasaje.update_pasaje(request, vm.pasaje)
        return Response(status=200, json_body={'msg':'Pasaje actualizado correctamente.'})
    except:
        return Response(status=400, json_body={'msg':'Pasaje no ha sido actualizado.'})

        
# Guarda un pasaje Editado
@view_config(route_name='add_pasaje',
             request_method='POST',
             permission="add")
def add_pasaje_api(request):

    try:
        pasaje_data = request.json_body
    except Exception as x:
        return Response(status=400, json_body={'msg': 'No se pudo parsear tu petición POST como un JSON: ' + str(x)})

    vm = CreatePasajeViewModel(pasaje_data)
    vm.compute_details()
    if vm.errors:
        return Response(status=400, json_body=vm.error_msg)
    try:
        pasaje = RepositorioPasaje.add_pasaje(request, vm.pasaje)
        return Response(status=200, json_body={'msg': 'Pasaje registrado correctamente'})
    except Exception as x:
        return Response(status=500, json_body={'msg': 'No se pudo guardar el pasaje: ' + str(x)})
