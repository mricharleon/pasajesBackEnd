from pasajes.models.sitio import Sitio


class RepositorioSitio:
    
    @classmethod
    def all_sitios(cls, request):
        query_sitios = request.dbsession.query(Sitio).filter_by().all()
        request.dbsession

        return query_sitios
    
    @classmethod
    def get_sitio(cls, request, id_sitio):
        query_sitio = request.dbsession.query(Sitio).filter(Sitio.id == id_sitio).first()

        return query_sitio
