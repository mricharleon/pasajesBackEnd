from pyramid.view import view_config

# Servicios
from .. api.grupos import RepositorioGrupo
from .. import constants as enum

@view_config(route_name='get_grupos',
             renderer='json',
             request_method='GET')
def api_get_grupos(request):
    
    user = request.session['user']
    if user.grupo.nombre == enum.Usuario.GRUPO_ADMINISTRADOR.value:
        grupos = RepositorioGrupo.grupos_administradores(request)
    elif user.grupo.nombre == enum.Usuario.GRUPO_COOPERATIVA.value:
        grupos = RepositorioGrupo.grupos_cooperativas(request, enum.Usuario.GRUPO_COOPERATIVA.value)

    return grupos
