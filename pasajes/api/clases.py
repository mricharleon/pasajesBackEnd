from pasajes.models.clase import Clase


class RepositorioClase:
    
    @classmethod
    def all_clases(cls, request):
        query_clases = request.dbsession.query(Clase).filter_by().all()

        return query_clases
