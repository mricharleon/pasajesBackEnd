from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    Boolean,
)
from sqlalchemy.orm import relationship, backref

from .meta import Base


class Grupo(Base):
    """ The SQLAlchemy declarative model class for a Grupo object. """
    __tablename__ = 'grupo'
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False) 

    # TODO verfiicar esta relacion
    menu = relationship('Menu', back_populates='grupo')

    def __json__(self, request):
        return {'id':self.id,
                'nombre':self.nombre,
                }
