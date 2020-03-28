from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Float,
    Text,
)
from sqlalchemy.orm import relationship, backref

from .meta import Base


class Boleto(Base):
    """ The SQLAlchemy declarative model class for a Boleto object. """
    __tablename__ = 'boletos'
    id = Column(Integer, primary_key=True)
    numero_asientos = Column(Integer, nullable=False)
    precio_total = Column(Float, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref=backref('boleto', uselist=False))

    pasaje_id = Column(ForeignKey('pasajes.id'), nullable=False)
    pasaje = relationship('Pasaje', backref='pasaje_boletos')

    def __json__(self, request):
        return {'id':self.id,
                'numero_asientos':self.numero_asientos,
                'precio_total':self.precio_total,
                'user':self.user,
                'pasaje':self.pasaje
                }