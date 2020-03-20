from pyramid.compat import escape
import re
from docutils.core import publish_parts

from pyramid.httpexceptions import (
    HTTPForbidden,
    HTTPFound,
    HTTPNotFound,
    )

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models

# Servicios
from .. api.pasajes import RepositorioPasaje
from .. api.usuarios import RepositorioUsario

import json

# regular expression used to find WikiWords
wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

def jsonDefault(object):
    return object.__dict__

@view_config(route_name='view_api',
             renderer='../templates/api.jinja2')
def view_api(request):
    # next_url = request.route_url('view_page', pagename='FrontPage')
    page = 'API'
    content = 'contenido'
    edit_url = 'url de edicion'
    paginas = RepositorioPasaje.all_pasajes(request)
    usuarios = RepositorioUsario.all_usuarios(request)
    return dict(page=page, content=content, edit_url=edit_url, paginas=paginas, usuarios=usuarios)
    # return HTTPFound(location=next_url)

@view_config(route_name='view_page', renderer='../templates/view.jinja2',
             permission='view')
def view_page(request):
    page = request.context.page
    
    def add_link(match):
        word = match.group(1)
        exists = request.dbsession.query(models.Page).filter_by(name=word).all()
        if exists:
            view_url = request.route_url('view_page', pagename=word)
            return '<a href="%s">%s</a>' % (view_url, escape(word))
        else:
            add_url = request.route_url('add_page', pagename=word)
            return '<a href="%s">%s</a>' % (add_url, escape(word))

    content = publish_parts(page.data, writer_name='html')['html_body']
    content = wikiwords.sub(add_link, content)
    edit_url = request.route_url('edit_page', pagename=page.name)
    paginas = RepositorioPasaje.all_pasajes(request)
    usuarios = RepositorioUsario.all_usuarios(request)
    
    return dict(page=page, content=content, edit_url=edit_url, paginas=paginas, usuarios=usuarios)

@view_config(route_name='edit_page', renderer='../templates/edit.jinja2',
             permission='edit')
def edit_page(request):
    page = request.context.page
    if 'form.submitted' in request.params:
        page.data = request.params['body']
        next_url = request.route_url('view_page', pagename=page.name)
        return HTTPFound(location=next_url)
    return dict(
        pagename=page.name,
        pagedata=page.data,
        save_url=request.route_url('edit_page', pagename=page.name),
        )

@view_config(route_name='add_page', renderer='../templates/edit.jinja2',
             permission='create')
def add_page(request):
    pagename = request.context.pagename
    if 'form.submitted' in request.params:
        body = request.params['body']
        page = models.Page(name=pagename, data=body)
        page.creator = request.user
        page.creator = (
            request.dbsession.query(models.User).filter_by(name='editor').one())
        request.dbsession.add(page)
        next_url = request.route_url('view_page', pagename=pagename)
        return HTTPFound(location=next_url)
    save_url = request.route_url('add_page', pagename=pagename)
    return dict(pagename=pagename, pagedata='', save_url=save_url)