from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Clase(Base):
    """ The SQLAlchemy declarative model class for a Clase object. """
    __tablename__ = 'clases'
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False, unique=True)
    descripcion = Column(Text, nullable=False)

    def __json__(self, request):
        return {'nombre':self.nombre,
                'descripcion':self.descripcion,
                'id':self.id}