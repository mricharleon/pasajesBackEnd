from dateutil.parser import parse

from .. models import Boleto
from .base_viewmodel import ViewModelBase


class CreateBoletoViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.boleto = None

    def compute_details(self):

        numero_asientos = self.data_dict.get('numero_asientos')
        precio_total = self.data_dict.get('precio_total')
        user_id = self.data_dict.get('user_id')
        pasaje_id = self.data_dict.get('pasaje_id')

        if numero_asientos is None:
            self.errors.append("Número de asientos, es requerido.")
        elif int(numero_asientos) <= 0:
            self.errors.append("Número de asientos, no debe ser negativo o cero.")
        if precio_total is None:
            self.errors.append("Precio total, es requerido.")
        elif precio_total < 0:
            self.errors.append("Precio total, no debe ser negativo.")
        if not user_id:
            self.errors.append("El usuario, es requerido.")
        if not pasaje_id:
            self.errors.append("El pasaje, es requerido.")


        if not self.errors:
            boleto = Boleto(numero_asientos=numero_asientos,
                            precio_total=precio_total, 
                            user_id=user_id,
                            pasaje_id=pasaje_id)
            self.boleto = boleto