from dateutil.parser import parse

from .. models import User, Grupo
from .base_viewmodel import ViewModelBase


class CreateUsuarioViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.usuario = None

    def compute_details(self):

        id = self.data_dict.get('id')
        username = self.data_dict.get('username')
        nombre = self.data_dict.get('nombre')
        apellido = self.data_dict.get('apellido')
        email = self.data_dict.get('email')

        if not username:
            self.errors.append("Username, es requerido.")
        if not nombre:
            self.errors.append("Nombre, es requerido.")
        if not apellido:
            self.errors.append("Apellido, es requerido.")
        if not email:
            self.errors.append("Email, es requerido.")

        if not self.errors:
            usuario = User(id=id,
                           username=username,
                           nombre=nombre, 
                           apellido=apellido,
                           email=email
                           )
            self.usuario = usuario
