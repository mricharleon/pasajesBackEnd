class ViewModelBase:
    def __init__(self):
        self.errors = []

    @property
    def error_msg(self):
        msg = 'Hay errores con su petición: \n' + \
              '\n'.join(self.errors)

        return msg