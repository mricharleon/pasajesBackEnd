from pyramid.view import view_config

# Servicios
from .. api.cooperativas import RepositorioCooperativa

@view_config(route_name='get_cooperativas',
             renderer='json')
def get_cooperativas_api(request):
    cooperativas = RepositorioCooperativa.all_cooperativas(request)
    return cooperativas

@view_config(route_name='get_cooperativa',
             renderer='json')
def get_cooperativa_api(request):
    id_cooperativa = request.matchdict['id_cooperativa']
    cooperativa = RepositorioCooperativa.get_cooperativa(request, id_cooperativa)
    return cooperativa