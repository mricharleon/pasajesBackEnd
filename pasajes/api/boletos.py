from pasajes.models.boleto import Boleto


class RepositorioBoleto:
    
    @classmethod
    def all_boletos(cls, request, id_usuario):
        query_boletos = request.dbsession.query(Boleto).filter(Boleto.user_id == id_usuario).all()

        return query_boletos
    
    @classmethod
    def get_boleto(cls, request, id_boleto):
        query_boleto = request.dbsession.query(Boleto).filter(Boleto.id == id_boleto).first()

        return query_boleto