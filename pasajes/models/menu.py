from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    Boolean,
    String,
)
from sqlalchemy.orm import relationship, backref

from .meta import Base


class Menu(Base):
    """ The SQLAlchemy declarative model class for a Menu object. """
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    url = Column(Text, nullable=False)  

    grupo_id = Column(Integer, ForeignKey('grupo.id'))
    grupo = relationship('Grupo', back_populates='menu')

    # Relacion One To Many
    item = relationship('Item', back_populates='menu')
    
    def __json__(self, request):
        return {'id': self.id,
                'nombre': self.nombre,
                'url': self.url,
                'item': self.item,
                }


class Item(Base):
    """ The SQLAlchemy declarative model class for a Item object. """
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    es_menu = Column(Boolean, default=False)

    menu_id = Column(Integer, ForeignKey('menu.id'))
    menu = relationship('Menu', back_populates='item')

    # Relacion One To Many
    subitem = relationship('SubItem', back_populates='item')

    def __json__(self, request):
        return {'id': self.id,
                'nombre': self.nombre,
                'url': self.url,
                'es_menu': self.es_menu,
                'subitem': self.subitem}

class SubItem(Base):
    """ The SQLAlchemy declarative model class for a SubItem object. """
    __tablename__ = 'subitem'

    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    url = Column(Text, nullable=False)

    item_id = Column(Integer, ForeignKey('item.id'))
    item = relationship('Item', back_populates='subitem')

    def __json__(self, request):
        return {'id': self.id,
                'nombre': self.nombre,
                'url': self.url}
