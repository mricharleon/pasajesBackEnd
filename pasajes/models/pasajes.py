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
    asientos_disponibles = Column(Integer, nullable=False)

    origen_sitio_id = Column(Integer, ForeignKey('sitios.id'), nullable=False)
    origen = relationship('Sitio', backref=backref('pasaje_origen', uselist=False), foreign_keys=[origen_sitio_id])
    
    destino_sitio_id = Column(Integer, ForeignKey('sitios.id'), nullable=False)
    destino = relationship('Sitio', backref=backref('pasaje_destino', uselist=False),  foreign_keys=[destino_sitio_id])

    unidad_id = Column(ForeignKey('unidades.id'), nullable=False)
    unidad = relationship('Unidad', backref='unidad_pasajes')

    def __json__(self, request):
        return {'id':self.id,
                'salida':self.salida.isoformat(),
                'llegada':self.llegada.isoformat(),
                'precio':self.precio,
                'asientos_disponibles':self.asientos_disponibles,
                'origen':self.origen,
                'destino':self.destino,
                'unidad':self.unidad
                }