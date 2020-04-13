from pyramid.view import view_config
from pyramid.response import Response
from json import loads

# Modelos
from .. import models
from ..viewmodels.create_boleto_viewmodel import CreateBoletoViewModel

# Servicios
from .. api.boletos import RepositorioBoleto
from .. api.pasajes import RepositorioPasaje


# Obtiene todos boletos de un usuario
@view_config(route_name='get_boletos',
             request_method='GET',
             renderer='json')
def get_boletos_api(request):

    id_usuario = request.user.id
    boletos = RepositorioBoleto.all_boletos(request, id_usuario)

    return boletos

# Obtiene el boleto a travez de su Id
@view_config(route_name='api_boleto',
             renderer='json')
def get_boleto_api(request):
    id_boleto = request.matchdict['id_boleto']
    boleto = RepositorioBoleto.get_boleto(request, id_boleto)
    return boleto

# Crea un boleto
@view_config(route_name='api_boletos',
             request_method='POST')
def add_boleto_api(request):
    try:
        boleto_data = request.json_body
    except Exception as x:
        return Response( status=400, json_body={'msg':'No se pudo parsear tu petición POST como un JSON: ' + str(x)} )

    id_usuario = request.user.id # id de usuario
    vm = CreateBoletoViewModel(id_usuario, boleto_data)
    vm.compute_details()
    if vm.errors:
        return Response(status=400, json_body=vm.error_msg)
    try:
        boleto = RepositorioBoleto.add_boleto(request, vm.boleto)
        return Response(status=200, json_body={'msg':'Boleto registrado correctamente'})
    except Exception as x:
        return Response(status=500, json_body={'msg':'No se pudo guardar el boleto: ' + str(x)})


# Elimina un boleto
@view_config(route_name='api_boleto',
             request_method='DELETE')
def delete_boleto_api(request):
    boleto_id = request.matchdict['id_boleto']
    boleto = RepositorioBoleto.get_boleto(request, boleto_id)

    if not boleto:
        msg = "El boleto con el Id: '{}' no fue encontrado.".format(boleto_id)
        return Response(status=404, json_body={'msg': msg})
    
    valid = RepositorioBoleto.compute_details_delete(request, boleto)
    
    if valid:
        try:
            RepositorioBoleto.delete_boleto(request, boleto_id)
            return Response(status=200, json_body={'msg':'Boleto eliminado correctamente.'})
        except:
            return Response(status=400, json_body={'msg':'No se pudo eliminar el boleto, revisa tu petición.'})
    else:
        return Response(status=400, json_body={'msg':'El boleto será eliminado únicamente con 5 horas de anticipación.'})
