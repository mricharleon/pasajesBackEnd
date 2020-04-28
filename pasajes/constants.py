from enum import Enum

class Codigo(int, Enum):
    """Clase que permite establecer valores por defecto para codigos generados 
    """
    TAMANIO_PASS_TEMPORAL = 12
    TAMANIO_COD_VERIFICACION = 36

class Usuario(Enum):
    GRUPO_ADMINISTRADOR = 'Administrador'
    GRUPO_COOPERATIVA = 'Cooperativa'
    GRUPO_CLIENTE = 'Cliente'

class FrontEnd(Enum):
    CLIENT_URL = 'http://localhost:9000'

