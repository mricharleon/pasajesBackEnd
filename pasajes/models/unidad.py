from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship, backref

from .meta import Base


class Unidad(Base):
    """ The SQLAlchemy declarative model class for a Unidad object. """
    __tablename__ = 'unidades'
    id = Column(Integer, primary_key=True)
    numero_asientos = Column(Integer, nullable=False)

    clase_id = Column(Integer, ForeignKey('clases.id'), nullable=False)
    clase = relationship('Clase', backref=backref('unidad', uselist=False))

    cooperativa_id = Column(ForeignKey('cooperativas.id'), nullable=False)
    cooperativa = relationship('Cooperativa', backref='cooperativa_unidades')

    def __json__(self, request):
        return {'id':self.id,
                'numero_asientos':self.numero_asientos,
                'clase':self.clase,
                'cooperativa':self.cooperativa}