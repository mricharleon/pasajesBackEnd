from dateutil.parser import parse

from .. models import Cooperativa
from .base_viewmodel import ViewModelBase


class CreateCooperativaViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.cooperativa = None

    def compute_details(self):

        id = self.data_dict.get('id')
        nombre = self.data_dict.get('nombre')

        if not nombre:
            self.errors.append("Nombre, es requerido.")

        if not self.errors:
            cooperativa = Cooperativa(id=id,
                                      nombre=nombre)
            self.cooperativa = cooperativa
