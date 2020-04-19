from pasajes.models.user import User


class RepositorioUsario:
    
    @classmethod
    def all_usuarios(cls, request):
        """Obtiene todos los usuarios que se encuentran en la base de datos
        """
        query_usuarios = request.dbsession.query(User).filter_by().all()

        return query_usuarios

    @classmethod
    def get_usuario(cls, request, id_usuario):
        """Obtiene un usuario a través de su Id
        """
        query_usuario = request.dbsession.query(User).filter(User.id == id_usuario).first()

        return query_usuario


    @classmethod
    def check_username(cls, request, username):
        """ Verifica si ya se encuentra un usuario registrado con un mismo username
        """
        user = request.dbsession.query(User).filter_by(username=username).all()
        if user:
            status_username = 'error'
            msg_username = 'El username ya existe! Por favor, elige otro'
        else:
            status_username = 'success'
            msg_username = 'Username disponible'

        return dict(status_username=status_username, msg_username=msg_username)


    @classmethod
    def check_email(cls, request, email):
        """ Verifica si ya se encuentra un usuario registrado con un mismo email
        """
        user = request.dbsession.query(User).filter_by(email=email).all()
        if user:
            status_email = 'error'
            msg_email = 'El email ya existe! Por favor, elige otro'
        else:
            status_email = 'success'
            msg_email = 'Email disponible'

        return dict(status_email=status_email, msg_email=msg_email)
