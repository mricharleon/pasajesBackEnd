from pasajes.models.pasajes import Pasaje

from datetime import datetime, timedelta
from dateutil.parser import parse



class RepositorioPasaje:
    
    @classmethod
    def all_pasajes(cls, request, fecha, origen, destino):
        fromDate = datetime.strptime(fecha, '%Y-%m-%d')
        toDate = datetime.strptime(fecha, '%Y-%m-%d') + timedelta(days=1)
        query_pasajes = request.dbsession.query(Pasaje).filter(Pasaje.salida.between(fromDate, toDate)).all()

        return query_pasajes
    
    @classmethod
    def get_pasaje(cls, request, id_pasaje):
        query_pasaje = request.dbsession.query(Pasaje).filter(Pasaje.id == id_pasaje).first()

        return query_pasaje