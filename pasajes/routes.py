from . permissions import editor_factory

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('view_api', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    # API
    # Autenticacion
    config.add_route('api_login', '/api/login')
    config.add_route('api_logout', '/api/logout')

    # Menu 
    config.add_route('get_menu',
                     '/api/menu')

    # Usuarios
    config.add_route('api_check_username',
                     '/api/check-username/{username}')
    config.add_route('api_check_email',
                     '/api/check-email/{email}')
    config.add_route('api_usuario',
                     '/api/usuario/{id_usuario}')

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
                     '/api/unidades',
                     factory=editor_factory)
    config.add_route('get_unidad',
                     '/api/unidad/{id_unidad}')

    # Pasajes
    config.add_route('get_all_pasajes',
                     '/api/all/pasajes',
                     factory=editor_factory)
    config.add_route('get_pasajes',
                     '/api/pasajes/{fecha}/{origen}/{destino}')
    config.add_route('get_pasaje', # Ruta para UPDATE, GET
                     '/api/pasaje/{id_pasaje}',
                     factory=editor_factory)
    config.add_route('add_pasaje',
                     '/api/pasaje',
                     factory=editor_factory)

    # Boletos
    config.add_route('get_boletos', # Ruta para get all
                     '/api/get-boletos')
    config.add_route('api_boletos', # Ruta para POST
                     '/api/boletos')
    config.add_route('api_boleto', # Ruta para GET y DELETE
                     '/api/boleto/{id_boleto}')
