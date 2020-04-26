import bcrypt
from random import SystemRandom

import distutils

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    Boolean,
)

from sqlalchemy.orm import relationship, backref

from .meta import Base

from .. import constants as enum


class User(Base):
    """ The SQLAlchemy declarative model class for a User object. """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False, unique=True)
    nombre = Column(Text, nullable=False)
    apellido = Column(Text, nullable=False)
    email = Column(Text, nullable=False, unique=True)
    activo = Column(Boolean, default=False)
    cod_verificacion = Column(Text, nullable=True)

    password_hash = Column(Text)

    grupo_id = Column(Integer, ForeignKey('grupo.id'), nullable=False)
    grupo = relationship('Grupo', lazy='subquery', backref=backref('user', uselist=False))

    def set_activo(self, estado):
        self.activo = estado
    
    def remove_cod_verificacion(self):
        self.cod_verificacion = None

    def set_password(self, pw):
        pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.password_hash = pwhash.decode('utf8')
        print(self.password_hash, pw)
    

    def set_cod_verificacion(self, cod):
        self.cod_verificacion = cod


    def check_password(self, pw):
        if self.password_hash is not None:
            expected_hash = self.password_hash.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
        return False
    
    
    def cambiar_password(self, pw_antiguo, pw_nuevo):
        try:
            self.check_password(pw_antiguo)
            self.set_password(pw_nuevo)
        except:
            return False
    

    def generar_codigo(self, tamanio):
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        crypto = SystemRandom()
        passw = ''
        for i in range(tamanio):
            passw = passw + crypto.choice(valores)
        return passw


    def generar_pass_temporal(self):
        pass_temporal = self.generar_codigo(enum.Codigo.TAMANIO_PASS_TEMPORAL.value)
        return pass_temporal
    

    def generar_cod_verificacion(self):
        pass_temporal = self.generar_codigo(enum.Codigo.TAMANIO_COD_VERIFICACION.value)
        return pass_temporal


    def enviar_mensaje(self, request, password, asunto=''):

        status = False
        msg = ''
        settings = request.registry.settings
        email_content = u"""<html>
                           <head>
                                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                           </head>
                           <body>
                           <div style="background-color: #f9f9f9;
                                       padding: 0 20px;
                                       color: #3e3e3e;
                                       border-radius: 30px 30px 0 0;">
                                <h3 style="background-color: #e06767;
                                           color: white;
                                           padding: 3px 6px;
                                           margin: 0px -10px !important;
                                           border-radius: 4px;
                                           text-align: center;">Hola, {0}</h3> 
                                <p>Acabas de crear una cuenta en el sistema de gestión de pasajes, Genial!</p>
                                <p>Al momento tu cuenta se encuentra en estado inactivo, debes seguir los siguientes pasos y estará activada.</p>
                                <div style="margin: 40px 0;">
                                    <p>Sus credenciales son:</p>
                                    <ul>
                                        <li>Usuario: {1}</li>
                                        <li>Contraseña: {2} <span style="color: #888888;">(Contraseña automática, podrá cambiarla mas adelante)</span></li>
                                    </ul>
                                </div>
                                <p>Para activar tu cuenta, abrir el siguiente enlace: <a href='{3}{4}' target='_blank'>Activar cuenta ahora!</a></p>
                                <hr>
                                <p style="background-color: #ececec;
                                          color: #7b7b7b;
                                          margin: 0px -10px !important;
                                          padding: 10px;
                                          text-align: center;">Este mensaje se ha generado de forma automática, no responder al mismo.</p>
                            </div>
                           </body>
                           </html>"""\
                        .format(self.nombre, 
                                self.username,
                                password,
                                enum.FrontEnd.HOST.value + 'activar/',
                                self.cod_verificacion
                                )
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Pasajes! - Creación de usuario {}'.format(asunto)
        msg['From'] = settings['email.sender']
        msg['To'] = self.email
        password = settings['email.password']
        msg.add_header('Content-Type', 'text/html; charset=utf-8')
        msg.attach( MIMEText(email_content, 'html') ) 
        server = smtplib.SMTP('{}: {}'.format(settings['email.host'], 
                                              settings['email.port'])
                                              )
        if distutils.util.strtobool( settings['email.tls'] ):
            server.starttls()
        if not server.login(msg['From'], password):
            status = False
            msg = 'No se pudo realizar el [login SMTP]'
        try:
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
            server.quit()
            status = True
            msg = 'Email enviado a [{}], por favor revisarlo para activar la cuenta'.format(self.email)
        except Exception as ex:
            status = False
            msg = 'No se pudo realizar el envió del mensaje {}'.format(ex)

        return dict(status=status, 
                    msg=msg)


    def __json__(self, request):
        return {'id': self.id,
                'username': self.username,
                'nombre': self.nombre,
                'apellido': self.apellido,
                'email': self.email,
                'activo': self.activo,
                'grupo': self.grupo.nombre,
               }
