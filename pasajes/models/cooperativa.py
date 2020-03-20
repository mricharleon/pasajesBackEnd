from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship

from .meta import Base


class Cooperativa(Base):
    """ The SQLAlchemy declarative model class for a Cooperativa object. """
    __tablename__ = 'cooperativas'
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False, unique=True)

    user_id = Column(ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='user_cooperativas')

    def __json__(self, request):
        return {'nombre':self.nombre,
                'id':self.id}