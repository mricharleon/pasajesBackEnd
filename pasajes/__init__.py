from pyramid.config import Configurator
from pyramid.events import NewRequest


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        allow_cors(config)
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')
        config.include('.security')
        config.scan()
    return config.make_wsgi_app()

def allow_cors(config):
    def add_cors_headers_response_callback(event):
        def cors_headers(_, response):
            # log.trace("Adding CORS permission to request: {}".format(
            #     request.url
            # ))
            response.headers.update({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
                'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
                'Access-Control-Allow-Credentials': 'true',
                'Access-Control-Max-Age': '1728000',
            })

        event.request.add_response_callback(cors_headers)

    config.add_subscriber(add_cors_headers_response_callback, NewRequest)