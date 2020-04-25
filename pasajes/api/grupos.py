from pasajes.models.grupo import Grupo


class RepositorioGrupo:
    
    @classmethod
    def grupos_administradores(cls, request):
        """Extrae todos los grupos que se encuentran registrados
        """
        query_grupos = request.dbsession.query(Grupo).all()

        return query_grupos

    @classmethod
    def grupos_cooperativas(cls, request, grupo_cooperativa):
        """Extrae todos los grupos de cooperativas
        """
        query_grupo = request.dbsession.query(Grupo).filter_by(nombre=grupo_cooperativa).first()

        return query_grupo

    @classmethod
    def get_grupo(cls, request, nombre_grupo):
        """Extrae un unico grupo
        """
        query_grupo = request.dbsession.query(Grupo).filter_by(nombre=nombre_grupo).first()

        return query_grupo
