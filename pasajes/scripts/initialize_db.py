import argparse
import sys
import datetime

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    
    # Grupo
    administrador = models.Grupo(nombre='Administrador')
    dbsession.add(administrador)
    cooperativa = models.Grupo(nombre='Cooperativa')
    dbsession.add(cooperativa)
    cliente = models.Grupo(nombre='Cliente')
    dbsession.add(cliente)

    # Menu
    menu1 = models.Menu(nombre='Boletos', url='', grupo=administrador)
    dbsession.add(menu1)
    menu2 = models.Menu(nombre='Pasajes', url='', grupo=administrador)
    dbsession.add(menu2)
    menu3 = models.Menu(nombre='Boletos', url='', grupo=cooperativa)
    dbsession.add(menu3)
    menu4 = models.Menu(nombre='Pasajes', url='', grupo=cooperativa)
    dbsession.add(menu4)
    menu5 = models.Menu(nombre='Boletos', url='', grupo=cliente)
    dbsession.add(menu5)
    menu6 = models.Menu(nombre='Cuentas', url='', grupo=administrador)
    dbsession.add(menu6)
    menu7 = models.Menu(nombre='Cuentas', url='', grupo=cooperativa)
    dbsession.add(menu7)

    # Item
    item1 = models.Item(nombre='Comprar boletos', url='#!/inicio', es_menu=False, menu=menu1)
    dbsession.add(item1)
    item2 = models.Item(nombre='Listar boletos comprados', url='#!/mis-boletos', es_menu=False, menu=menu1)
    dbsession.add(item2)
    item_crear = models.Item(nombre='Crear pasaje', url='#!/add-pasaje', es_menu=False, menu=menu2)
    dbsession.add(item_crear)
    item3 = models.Item(nombre='Listar pasajes', url='#!/list-pasajes', es_menu=False, menu=menu2)
    dbsession.add(item3)
    item4 = models.Item(nombre='Comprar boletos', url='#!/inicio', es_menu=False, menu=menu3)
    dbsession.add(item4)
    item5 = models.Item(nombre='Listar boletos comprados', url='#!/mis-boletos', es_menu=False, menu=menu3)
    dbsession.add(item5)
    item_crear = models.Item(nombre='Crear pasaje', url='#!/add-pasaje', es_menu=False, menu=menu4)
    dbsession.add(item_crear)
    item6 = models.Item(nombre='Listar pasajes', url='#!/list-pasajes', es_menu=False, menu=menu4)
    dbsession.add(item6)
    item7 = models.Item(nombre='Comprar boletos', url='#!/inicio', es_menu=False, menu=menu5)
    dbsession.add(item7)
    item8 = models.Item(nombre='Listar boletos comprados', url='#!/mis-boletos', es_menu=False, menu=menu5)
    dbsession.add(item8)
    item9 = models.Item(nombre='Crear cuentas', url='#!/registro', es_menu=False, menu=menu6)
    dbsession.add(item9)
    item10 = models.Item(nombre='Crear cuentas', url='#!/registro', es_menu=False, menu=menu7)
    dbsession.add(item10)

    # User
    u_administrador = models.User(username='admin', 
                                  nombre='Admin', 
                                  apellido='Admin', 
                                  email='admin@gmail.com', 
                                  grupo=administrador)
    u_administrador.set_password('admin')
    dbsession.add(u_administrador)
    cooperativa_loja = models.User(username='loja', 
                                   nombre='Loja',
                                   apellido='Loja', 
                                   email='loja@gmail.com', 
                                   grupo=cooperativa)
    cooperativa_loja.set_password('loja')
    dbsession.add(cooperativa_loja)
    cooperativa_cariamanga = models.User(username='cariamanga', 
                                         nombre='Cariamanga',
                                         apellido='Cariamanga', 
                                         email='cariamanga@gmail.com', 
                                         grupo=cooperativa)
    cooperativa_cariamanga.set_password('cariamanga')
    dbsession.add(cooperativa_cariamanga)
    basic = models.User(username='juan', 
                        nombre='Juan', 
                        apellido='Perez', 
                        email='juanperez@gmail.com', 
                        grupo=cliente)
    basic.set_password('juan')
    dbsession.add(basic)

    # Sitio
    loja = models.Sitio(ciudad='Loja', terminal='Av. Isidro Ayora')
    dbsession.add(loja)
    quito = models.Sitio(ciudad='Quito', terminal='Quitumbe')
    dbsession.add(quito)
    cuenca = models.Sitio(ciudad='Cuenca', terminal='Av. España y Sebastian de Benalcazar')
    dbsession.add(cuenca)
    guayaquil = models.Sitio(ciudad='Guayaquil', terminal='Río Daule')
    dbsession.add(guayaquil)

    # Cooperativa
    cooperativa_loja = models.Cooperativa(nombre='Cooperativa Loja', user=cooperativa_loja)
    dbsession.add(cooperativa_loja)
    cooperativa_cariamanga = models.Cooperativa(nombre='Cooperativa Cariamanga', user=cooperativa_cariamanga)
    dbsession.add(cooperativa_cariamanga)

    # Clase
    vip = models.Clase(nombre='VIP', descripcion='Clase VIP')
    dbsession.add(vip)
    normal = models.Clase(nombre='Normal', descripcion='Clase normal')
    dbsession.add(normal)

    # Unidad
    loja_1 = models.Unidad(numero_asientos=45, numero_unidad=1, clase=vip, cooperativa=cooperativa_loja)
    dbsession.add(loja_1)
    cariamanga_1 = models.Unidad(numero_asientos=40, numero_unidad=1, clase=normal, cooperativa=cooperativa_cariamanga)
    dbsession.add(cariamanga_1)
    cariamanga_2 = models.Unidad(numero_asientos=45, numero_unidad=2, clase=vip, cooperativa=cooperativa_cariamanga)
    dbsession.add(cariamanga_2)

    # Pasaje
    loja_quito_1 = models.Pasaje(salida=datetime.datetime.utcnow(),
                               llegada=datetime.datetime.utcnow(),
                               precio=20.5,
                               asientos_disponibles=45,
                               origen=loja,
                               destino=quito,
                               unidad=loja_1)
    dbsession.add(loja_quito_1)
    loja_quito_2 = models.Pasaje(salida=datetime.datetime.utcnow(),
                               llegada=datetime.datetime.utcnow(),
                               precio=20,
                               asientos_disponibles=40,
                               origen=loja,
                               destino=quito,
                               unidad=cariamanga_1)
    dbsession.add(loja_quito_2)
    loja_guayaquil = models.Pasaje(salida=datetime.datetime.utcnow(),
                                   llegada=datetime.datetime.utcnow(),
                                   precio=18,
                                   asientos_disponibles=45,
                                   origen=loja,
                                   destino=guayaquil,
                                   unidad=loja_1)
    dbsession.add(loja_guayaquil)
    loja_cuenca = models.Pasaje(salida=datetime.datetime.utcnow(),
                               llegada=datetime.datetime.utcnow(),
                               precio=8,
                               asientos_disponibles=45,
                               origen=loja,
                               destino=cuenca,
                               unidad=cariamanga_2)
    dbsession.add(loja_cuenca)

    # Boleto
    boleto_1 = models.Boleto(numero_asientos=2, precio_total=10.5, user=basic, pasaje=loja_quito_1)
    dbsession.add(boleto_1)
    boleto_2 = models.Boleto(numero_asientos=3, precio_total=12.5, user=basic, pasaje=loja_guayaquil)
    dbsession.add(boleto_2)
    boleto_3 = models.Boleto(numero_asientos=25, precio_total=15, user=basic, pasaje=loja_cuenca)
    dbsession.add(boleto_3)




def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            ''')
