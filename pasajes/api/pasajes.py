from pasajes.models.pasajes import Pasaje

from datetime import datetime, timedelta
from dateutil.parser import parse



class RepositorioPasaje:
    
    @classmethod
    def get_all_pasajes(cls, request):
        query_pasajes = request.dbsession.query(Pasaje).filter().order_by(Pasaje.origen_sitio_id).all()

        return query_pasajes

    @classmethod
    def all_pasajes(cls, request, fecha, origen, destino):
        fromDate = datetime.strptime(fecha, '%Y-%m-%d')
        toDate = datetime.strptime(fecha, '%Y-%m-%d') + timedelta(days=1)
        query_pasajes = request.dbsession.query(Pasaje).filter(Pasaje.salida.between(fromDate, toDate))\
                                                       .filter(Pasaje.origen_sitio_id == origen)\
                                                       .filter(Pasaje.destino_sitio_id == destino)\
                                                       .all()

        return query_pasajes
    
    @classmethod
    def get_pasaje(cls, request, id_pasaje):
        query_pasaje = request.dbsession.query(Pasaje).filter(Pasaje.id == id_pasaje).first()

        return query_pasaje