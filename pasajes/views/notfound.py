from pyramid.view import notfound_view_config
from pyramid.response import Response


@notfound_view_config(renderer='json')
def notfound_view(request):

    msg = 'Página no encontrada!'
    
    return Response(status=404, json_body={ 'msg':msg })
