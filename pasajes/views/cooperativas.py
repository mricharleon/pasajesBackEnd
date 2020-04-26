from pyramid.view import view_config
from pyramid.response import Response

# Servicios
from .. api.cooperativas import RepositorioCooperativa

from ..viewmodels.create_cooperativa_viewmodel import CreateCooperativaViewModel

from .. models import Cooperativa


@view_config(route_name='get_cooperativas',
             renderer='json',
             request_method='GET')
def get_cooperativas_api(request):
    cooperativas = RepositorioCooperativa.all_cooperativas(request)
    return cooperativas


@view_config(route_name='get_cooperativa',
             renderer='json')
def get_cooperativa_api(request):
    id_cooperativa = request.matchdict['id_cooperativa']
    cooperativa = RepositorioCooperativa.get_cooperativa(request, id_cooperativa)
    return cooperativa


@view_config(route_name='cooperativas',
             renderer='json',
             request_method='POST')
def add_cooperativa_api(request):
    try:
        cooperativa_data = request.json_body
    except Exception as x:
        return Response(status=400, json_body={'titulo': 'Petición errónea!',
                                               'msg': 'No se pudo parsear tu petición POST como un JSON: ' + str(x)})

    vm = CreateCooperativaViewModel(cooperativa_data)
    vm.compute_details()
    if vm.errors:
        return Response(status=400, json_body=vm.error_msg)

    # Consulta si existe una cooperativa asignada al usuario solicitante
    user = request.session.get('user')
    if request.dbsession.query(Cooperativa).filter_by(user=user).first() is not None:
        c = request.dbsession.query(Cooperativa).filter_by(user=user).first()
        return Response(status=400, json_body={'titulo':'Ya existe una cooperativa!',
                                               'msg':'Actualmente tienes una cooperativa [{}] registrada'.format(c.nombre)})

    user = request.session.get('user')
    vm.cooperativa.user_id = user.id

    try:
        cooperativa = RepositorioCooperativa.add_cooperativa(request, vm.cooperativa)
        return Response(status=200, json_body={'titulo': 'Cooperativa registrada!',
                                               'msg': ''})
    except Exception as x:
        return Response(status=400, json_body={'titulo': 'Sucedio algo inesperado!',
                                               'msg': 'No se pudo guardar la cooperativa: ' + str(x)})
