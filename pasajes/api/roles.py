from pasajes.models.rol import Rol


class RepositorioRol:
    
    @classmethod
    def all_roles(cls, request):
        query_roles = request.dbsession.query(Rol).filter_by().all()

        return query_roles
