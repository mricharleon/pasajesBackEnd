import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    Float,
    DateTime,
)
from sqlalchemy.orm import relationship, backref

from .meta import Base


class Pasaje(Base):
    """ The SQLAlchemy declarative model class for a Pasaje object. """
    __tablename__ = 'pasajes'
    id = Column(Integer, primary_key=True)
    salida = Column(DateTime, default=datetime.datetime.utcnow)
    llegada = Column(DateTime, default=datetime.datetime.utcnow)
    precio = Column(Float, nullable=False)

    sitio_id = Column(Integer, ForeignKey('sitios.id'), nullable=False)
    origen = relationship('Sitio', backref=backref('pasaje_origen', uselist=False))
    
    sitio_id = Column(Integer, ForeignKey('sitios.id'), nullable=False)
    destino = relationship('Sitio', backref=backref('pasaje_destino', uselist=False))

    unidad_id = Column(ForeignKey('unidades.id'), nullable=False)
    unidad = relationship('Unidad', backref='unidad_pasajes')

    def __json__(self, request):
        return {'salida':self.salida,
                'llegada':self.llegada,
                'precio':self.precio,
                'id':self.id}