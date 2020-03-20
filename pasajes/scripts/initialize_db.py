import argparse
import sys
import datetime

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    # Rol
    admin = models.Rol(nombre='admin', descripcion='Usuario administrador')
    dbsession.add(admin)
    cliente = models.Rol(nombre='cliente', descripcion='Usuario cliente')
    dbsession.add(cliente)

    # User
    editor = models.User(name='editor', role='editor', rol=admin)
    editor.set_password('editor')
    dbsession.add(editor)
    basic = models.User(name='basic', role='basic', rol=cliente)
    basic.set_password('basic')
    dbsession.add(basic)

    # Pagina 
    page = models.Page(
        name='FrontPage',
        creator=editor,
        data='This is the front page',
    )
    dbsession.add(page)

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
    cooperativa_loja = models.Cooperativa(nombre='Cooperativa Loja', user=editor)
    dbsession.add(cooperativa_loja)
    cooperativa_cariamanga = models.Cooperativa(nombre='Cooperativa Cariamanga', user=editor)
    dbsession.add(cooperativa_cariamanga)

    # Clase
    vip = models.Clase(nombre='VIP', descripcion='Clase VIP')
    dbsession.add(vip)
    normal = models.Clase(nombre='Normal', descripcion='Clase normal')
    dbsession.add(normal)

    # Unidad
    loja_1 = models.Unidad(numero_asientos=45, clase=vip, cooperativa=cooperativa_loja)
    dbsession.add(loja_1)
    cariamanga_1 = models.Unidad(numero_asientos=40, clase=normal, cooperativa=cooperativa_cariamanga)
    dbsession.add(cariamanga_1)
    cariamanga_2 = models.Unidad(numero_asientos=45, clase=vip, cooperativa=cooperativa_cariamanga)
    dbsession.add(cariamanga_2)

    # Pasaje
    loja_quito_1 = models.Pasaje(salida=datetime.datetime.utcnow(),
                               llegada=datetime.datetime.utcnow(),
                               precio=20.5,
                               origen=loja,
                               destino=quito,
                               unidad=loja_1)
    dbsession.add(loja_quito_1)
    loja_quito_2 = models.Pasaje(salida=datetime.datetime.utcnow(),
                               llegada=datetime.datetime.utcnow(),
                               precio=20,
                               origen=loja,
                               destino=quito,
                               unidad=cariamanga_1)
    dbsession.add(loja_quito_2)
    loja_guayaquil = models.Pasaje(salida=datetime.datetime.utcnow(),
                                   llegada=datetime.datetime.utcnow(),
                                   precio=18,
                                   origen=loja,
                                   destino=guayaquil,
                                   unidad=loja_1)
    dbsession.add(loja_guayaquil)
    loja_cuenca = models.Pasaje(salida=datetime.datetime.utcnow(),
                               llegada=datetime.datetime.utcnow(),
                               precio=8,
                               origen=loja,
                               destino=cuenca,
                               unidad=cariamanga_2)
    dbsession.add(loja_cuenca)

    # Boleto
    boleto_1 = models.Boleto(numero_asientos='1,2,3', user=basic, pasaje=loja_quito_1)
    dbsession.add(boleto_1)
    boleto_2 = models.Boleto(numero_asientos='15,16', user=basic, pasaje=loja_guayaquil)
    dbsession.add(boleto_2)
    boleto_3 = models.Boleto(numero_asientos='25', user=basic, pasaje=loja_cuenca)
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
