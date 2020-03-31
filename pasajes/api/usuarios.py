from pasajes.models.user import User


class RepositorioUsario:
    
    @classmethod
    def all_usuarios(cls, request):
        query_usuarios = request.dbsession.query(User).filter_by().all()

        return query_usuarios

    @classmethod
    def get_usuario(cls, request, id_usuario):
        query_usuario = request.dbsession.query(User).filter(User.id == id_usuario).first()

        return query_usuario