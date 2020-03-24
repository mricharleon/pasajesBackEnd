from pasajes.models.cooperativa import Cooperativa


class RepositorioCooperativa:
    
    @classmethod
    def all_cooperativas(cls, request):
        query_cooperativas = request.dbsession.query(Cooperativa).filter_by().all()

        return query_cooperativas
    
    @classmethod
    def get_cooperativa(cls, request, id_cooperativa):
        query_cooperativa = request.dbsession.query(Cooperativa).filter(Cooperativa.id == id_cooperativa).first()

        return query_cooperativa
