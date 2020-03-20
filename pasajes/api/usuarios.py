from pasajes.models.user import User


class RepositorioUsario:
    
    @classmethod
    def all_usuarios(cls, request):
        query_usuarios = request.dbsession.query(User).filter_by().all()

        return query_usuarios