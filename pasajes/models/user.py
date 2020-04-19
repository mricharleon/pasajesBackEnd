import bcrypt
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
)

from sqlalchemy.orm import relationship, backref

from .meta import Base


class User(Base):
    """ The SQLAlchemy declarative model class for a User object. """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False, unique=True)
    nombre = Column(Text, nullable=False)
    apellido = Column(Text, nullable=False)
    email = Column(Text, nullable=False, unique=True)

    password_hash = Column(Text)

    grupo_id = Column(Integer, ForeignKey('grupo.id'), nullable=False)
    grupo = relationship('Grupo', lazy='subquery', backref=backref('user', uselist=False))

    def set_password(self, pw):
        pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.password_hash = pwhash.decode('utf8')

    def check_password(self, pw):
        if self.password_hash is not None:
            expected_hash = self.password_hash.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
        return False

    def __json__(self, request):
        return {'id': self.id,
                'username': self.username,
                'nombre':self.nombre,
                'apellido':self.apellido,
                'email':self.email,
               }
