from pyramid.view import view_config

# Servicios
from .. api.boletos import RepositorioBoleto

@view_config(route_name='get_boletos',
             renderer='json')
def get_boletos_api(request):
    id_usuario = request.matchdict['id_usuario']
    boletos = RepositorioBoleto.all_boletos(request, id_usuario)
    return boletos

@view_config(route_name='get_boleto',
             renderer='json')
def get_boleto_api(request):
    id_boleto = request.matchdict['id_boleto']
    boleto = RepositorioBoleto.get_boleto(request, id_boleto)
    return boleto