from dateutil.parser import parse

from .. models import Pasaje
from .base_viewmodel import ViewModelBase


class CreatePasajeViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.boleto = None

    def compute_details(self):

        id = self.data_dict.get('id')
        salida = self.data_dict.get('salida')
        llegada = self.data_dict.get('llegada')
        precio = self.data_dict.get('precio')
        asientos_disponibles = self.data_dict.get('asientos_disponibles')
        origen_sitio_id = self.data_dict.get('origen_id')
        destino_sitio_id = self.data_dict.get('destino_id')
        unidad_id = self.data_dict.get('unidad_id')

        if not salida:
            self.errors.append("Fecha de salida, es requerido.")
        if llegada is None:
            self.errors.append("Fecha de llegada, es requerido.")
        if precio is None:
            self.errors.append("Precio, es requerido.")
        elif precio < 0:
            self.errors.append("Precio, no debe ser negativo.")
        if asientos_disponibles is None:
            self.errors.append("Asientos disponibles, es requerido.")
        elif asientos_disponibles < 0:
            self.errors.append("Asientos disponibles, no debe ser negativo.")
        if not origen_sitio_id:
            self.errors.append("Origen, es requerido.")
        if not destino_sitio_id:
            self.errors.append("Destino, es requerido.")
        if not unidad_id:
            self.errors.append("Unidad, es requerido.")

        if not self.errors:
            pasaje = Pasaje(id=id,
                            salida=salida,
                            llegada=llegada, 
                            precio=precio,
                            asientos_disponibles=asientos_disponibles,
                            origen_sitio_id=origen_sitio_id,
                            destino_sitio_id=destino_sitio_id,
                            unidad_id=unidad_id)
            self.pasaje = pasaje