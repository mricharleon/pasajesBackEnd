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
    page = 'API'
    content = 'contenido'
    edit_url = 'url de edicion'
    return dict(page=page, content=content)