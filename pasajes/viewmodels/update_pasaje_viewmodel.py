from dateutil.parser import parse

from ..models import Pasaje
from .base_viewmodel import ViewModelBase
from .create_pasaje_viewmodel import CreatePasajeViewModel


class UpdatePasajeViewModel(CreatePasajeViewModel):
    def __init__(self, data_dict, pasaje_id):
        super().__init__(data_dict)
        self.pasaje_id = int(pasaje_id)

    def compute_details(self):

        pasaje_id = self.data_dict.get('id')
        if not self.pasaje_id:
            self.errors.append("No se especifica el Id del pasaje.")
        if self.pasaje_id != pasaje_id:
            self.errors.append("El Id del pasaje no coincide.")

        super().compute_details()