import os

from pyramid.config import Configurator
from pyramid.events import NewRequest

from pyramid_redis_sessions import session_factory_from_settings

from . import constants as enum


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    with Configurator(settings=settings) as config:
        session_factory = session_factory_from_settings(settings)
        allow_cors(config)
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')
        config.include('.security')
        config.set_session_factory(session_factory)
        config.include('pyramid_redis_sessions')
        config.scan()
    return config.make_wsgi_app()

def allow_cors(config):
    def add_cors_headers_response_callback(event):
        def cors_headers(_, response):
            # log.trace("Adding CORS permission to request: {}".format(
            #     request.url
            # ))
            # Importa la variable de client_url
            CLIENT_URL = os.environ['CLIENT_URL'] if ('CLIENT_URL' in os.environ) else enum.FrontEnd.CLIENT_URL.value
            response.headers.update({
                'Access-Control-Allow-Origin': CLIENT_URL,
                'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,HEAD,OPTIONS',
                'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Accept-Language, X-Request-ID,Authorization',
                'Access-Control-Allow-Credentials': 'true',
                'Access-Control-Max-Age': '1728000',
            })

        event.request.add_response_callback(cors_headers)

    config.add_subscriber(add_cors_headers_response_callback, NewRequest)
