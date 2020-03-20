from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Sitio(Base):
    """ The SQLAlchemy declarative model class for a Sitio object. """
    __tablename__ = 'sitios'
    id = Column(Integer, primary_key=True)
    ciudad = Column(Text, nullable=False)
    terminal = Column(Text, nullable=False)

    def __json__(self, request):
        return {'ciudad':self.ciudad,
                'terminal':self.terminal,
                'id':self.id}