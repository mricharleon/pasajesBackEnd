from datetime import datetime, timedelta
from pasajes.models.boleto import Boleto
from .pasajes import RepositorioPasaje


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

        # Decrementa el numero de asientos disponibles en el pasaje
        pasaje = RepositorioPasaje.get_pasaje(request, boleto.pasaje_id)
        asientos_disponibles = pasaje.asientos_disponibles - int(boleto.numero_asientos)
        pasaje.asientos_disponibles = asientos_disponibles

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
            return

        request.dbsession.delete(db_boleto)        
        return

    @classmethod
    def compute_details_delete(cls, request, boleto):
        """Verifica que cumpla con las condiciones necesarias para poder ser eliminado
        - si la fecha actual es menos o igual a 5 horas de la fecha de salida del boleto
        """

        pasaje = RepositorioPasaje.get_pasaje(request, boleto.pasaje_id)
        fecha_cinco_horas_mas = datetime.now() + timedelta(hours=5)

        if fecha_cinco_horas_mas <= pasaje.salida:
            try:
                pasaje.asientos_disponibles += boleto.numero_asientos
                return True
            except:
                return None 
        return None 
