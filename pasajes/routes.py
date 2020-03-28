from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound,
)
from pyramid.security import (
    Allow,
    Everyone,
)

from . import models

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('view_api', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    # API
    # Rol
    config.add_route('get_roles',
                     '/api/roles')
    # Sitio
    config.add_route('get_sitios',
                     '/api/sitios')
    config.add_route('get_sitio',
                     '/api/sitio/{id_sitio}')
    # Cooperativa
    config.add_route('get_cooperativas',
                     '/api/cooperativas')
    config.add_route('get_cooperativa',
                     '/api/cooperativa/{id_cooperativa}')
    # Clase
    config.add_route('get_clases',
                     '/api/clases')
    config.add_route('add_clase',
                     '/api/clase')
    # Unidad
    config.add_route('get_unidades',
                     '/api/unidades')
    config.add_route('get_unidad',
                     '/api/unidad/{id_unidad}')
    # Pasajes
    config.add_route('get_all_pasajes',
                     '/api/all/pasajes')
    config.add_route('get_pasajes',
                     '/api/pasajes/{fecha}/{origen}/{destino}')
    config.add_route('get_pasaje',
                     '/api/pasaje/{id_pasaje}')
    config.add_route('add_edit_pasaje',
                     '/api/pasaje/edit')
    # Boletos
    config.add_route('get_boletos',
                     '/api/boletos/{id_usuario}',)
    config.add_route('get_boleto',
                     '/api/boleto/{id_boleto}')
    config.add_route('add_boleto',
                     'api/boleto2')
    

    # Solo quedan como respaldo
    config.add_route('view_page', '/{pagename}', factory=page_factory)
    config.add_route('add_page', '/add_page/{pagename}',
                     factory=new_page_factory)
    config.add_route('edit_page', '/{pagename}/edit_page',
                     factory=page_factory)



def new_page_factory(request):
    pagename = request.matchdict['pagename']
    if request.dbsession.query(models.Page).filter_by(name=pagename).count() > 0:
        next_url = request.route_url('edit_page', pagename=pagename)
        raise HTTPFound(location=next_url)
    return NewPage(pagename)

class NewPage(object):
    def __init__(self, pagename):
        self.pagename = pagename

    def __acl__(self):
        return [
            (Allow, 'role:editor', 'create'),
            (Allow, 'role:basic', 'create'),
        ]

def page_factory(request):
    pagename = request.matchdict['pagename']
    page = request.dbsession.query(models.Page).filter_by(name=pagename).first()
    if page is None:
        raise HTTPNotFound
    return PageResource(page)

class PageResource(object):
    def __init__(self, page):
        self.page = page

    def __acl__(self):
        return [
            (Allow, Everyone, 'view'),
            (Allow, 'role:editor', 'edit'),
            (Allow, str(self.page.creator_id), 'edit'),
        ]

def api_pasajes_factory(request):
    return PasajeResource()

class PasajeResource(object):
    def __init__(self):
        pass

    def __acl__(self):
        return [
            (Allow, 'role:editor', 'view'),
            (Allow, Everyone, 'view'),
        ]