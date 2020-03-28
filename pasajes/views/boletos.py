from pyramid.view import view_config
from pyramid.response import Response

# Modelos
from .. import models

# Servicios
from .. api.boletos import RepositorioBoleto
from .. api.pasajes import RepositorioPasaje


# Obtiene todos boletos de un usuario
@view_config(route_name='get_boletos',
             renderer='json')
def get_boletos_api(request):
    id_usuario = request.matchdict['id_usuario']
    boletos = RepositorioBoleto.all_boletos(request, id_usuario)
    return boletos

# Obtiene el boleto a travez de su Id
@view_config(route_name='get_boleto',
             renderer='json')
def get_boleto_api(request):
    id_boleto = request.matchdict['id_boleto']
    boleto = RepositorioBoleto.get_boleto(request, id_boleto)
    return boleto

# Crea un boleto
@view_config(route_name='add_boleto',
             request_method='POST',
             renderer='json')
def add_boleto_api(request):
    dataBoleto = request.json_body
    boleto = models.Boleto(numero_asientos=dataBoleto.get('numero_asientos'),
                           precio_total=dataBoleto.get('precio_total'),
                           user_id=dataBoleto.get('user_id'),
                           pasaje_id=dataBoleto.get('pasaje_id'))

    # Actualiza el valor de asientos disponibles en el pasaje
    pasaje = RepositorioPasaje.get_pasaje(request, boleto.pasaje_id)
    if (pasaje.unidad.numero_asientos >= int(boleto.numero_asientos)):
        asientos_disponibles = pasaje.asientos_disponibles - int(boleto.numero_asientos)
        pasaje.asientos_disponibles = asientos_disponibles
    else:
        asientos_disponibles = False
    
    if (request.dbsession.add(boleto) == None) and (request.dbsession.add(pasaje) == None) and asientos_disponibles:
        response = {
            'msg': 'Boleto registrado correctamente!',
            'status': '200',
        }
    else:
        response = {
            'msg': 'Error, Boleto no registrado!',
            'status': '422',
        }
    return response