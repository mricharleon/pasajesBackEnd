from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from json import loads

# Modelos
from .. import models

# Servicios
from .. api.menu import RepositorioMenu
from .. api.usuarios import RepositorioUsario


# Obtiene el menu de acuerdo al usuario que este logueado
@view_config(route_name='get_menu',
             renderer='json',
             request_method='GET')
def get_menu_api(request):

    id_usuario = request.session.get('user').id
    usuario = RepositorioUsario.get_usuario(request, id_usuario)
    menu = RepositorioMenu.get_menu(request, usuario)

    return menu
