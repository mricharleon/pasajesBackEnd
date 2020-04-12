from pasajes.models.menu import Menu
from pasajes.models.grupo import Grupo

from datetime import datetime, timedelta
from dateutil.parser import parse


class RepositorioMenu:
    
    @classmethod
    def get_menu(cls, request, usuario):
        query_menu = request.dbsession.query(Menu).filter(Menu.grupo_id == usuario.grupo_id).all()

        return query_menu