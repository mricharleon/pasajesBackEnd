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

    @classmethod
    def add_boleto(cls, request, boleto: Boleto):
        db_boleto = Boleto()
        db_boleto.numero_asientos = boleto.numero_asientos
        db_boleto.precio_total = boleto.precio_total
        db_boleto.user_id = boleto.user_id
        db_boleto.pasaje_id = boleto.pasaje_id

        request.dbsession.add(db_boleto)

        return db_boleto

    @classmethod
    def delete_boleto(cls, request, boleto_id):
        db_boleto = request.dbsession.query(Boleto).filter(Boleto.id == boleto_id).first()
        if not db_boleto:
            print('hola')
            return

        request.dbsession.delete(db_boleto)        
        return