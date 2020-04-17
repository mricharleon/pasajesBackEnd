from pasajes.models.unidad import Unidad
from pasajes.models.cooperativa import Cooperativa
from pasajes.models.clase import Clase

from sqlalchemy.orm import load_only


class RepositorioUnidad:
    
    @classmethod
    def all_unidades(cls, request):
        """Extrae todas las unidades que se encuentran registradas independiente 
        del usuario logueado
        """
        query_unidades = request.dbsession.query(Unidad).filter_by().all()

        return query_unidades

    @classmethod
    def all_unidades_usuario(cls, request, id_usuario):
        """Extrae todas las unidades que pertenecen al usuario de tipo cooperttiva
        que se encuentra logueado
        """
        query_unidades = request.dbsession.query(Unidad).join(Cooperativa).filter(
            Cooperativa.user_id == id_usuario).all()

        return query_unidades
    
    @classmethod
    def get_unidad(cls, request, id_unidad):
        """Extrae un objeto unidad a través de su id
        """
        query_unidad = request.dbsession.query(Unidad).filter(Unidad.id == id_unidad).first()

        return query_unidad
