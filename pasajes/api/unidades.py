from pasajes.models.unidad import Unidad
from pasajes.models.clase import Clase

from sqlalchemy.orm import load_only


class RepositorioUnidad:
    
    @classmethod
    def all_unidades(cls, request):
        query_unidades = request.dbsession.query(Unidad).filter_by().all()

        return query_unidades
    
    @classmethod
    def get_unidad(cls, request, id_unidad):
        query_unidad = request.dbsession.query(Unidad).filter(Unidad.id == id_unidad).first()

        return query_unidad