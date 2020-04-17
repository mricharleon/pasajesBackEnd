from pyramid.security import (
    Allow,
    Everyone, 
)

def editor_factory(request):
    return EditorResource()


class EditorResource(object):
    def __init__(self):
        pass

    def __acl__(self):
        return [
            (Allow, 'grupo:Administrador', ['view', 'edit', 'add']),
            (Allow, 'grupo:Cooperativa', ['view', 'edit', 'add']),
            (Allow, 'grupo:Cliente', 'view'),
        ]
