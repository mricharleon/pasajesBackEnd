pasajesBackEnd
======

## Clonar el proyecto y crear entorno virtual

~~~
git clone git@github.com:mricharleon/pasajesBackEnd.git
cd pasajesBackEnd
virtualenv envPasajes --python=python3
~~~

## Activar entorno virtual y actualizar herramientas
~~~
source envPasajes/bin/activate
pip install --upgrade pip setuptools
~~~

## Instalar dependencias para desarrollo
~~~
pip install -e ".[testing]"
~~~

## Configrar e inicializar la base de datos
* sqlalchemy.url = postgresql://USERDB:PASSWORD@HOST:PORT/NAMEDB
~~~
alembic -c development.ini revision --autogenerate -m "init"
alembic -c development.ini upgrade head
initialize_pasajes_db development.ini
~~~

## Ejecutar Redis y el proyecto
~~~
redis-server
pserve development.ini 
~~~

## Recursos
| Endpoint | HTTP | Descripción |
|---|---|---|
| /api/login | POST | Crea una sesion, auth_tkt en el proyecto |
| /api/logout | GET | Cierra una sesion en el proyecto |
| /api/roles | GET | Obtiene todos los objetos roles |
| /api/usuario/{id_usuario} | GET | Obtiene un solo objeto usuario |
| /api/sitios | GET | Obtiene todos los objetos de sitios |
| /api/sitio/{id_sitio} | GET | Obtiene un solo objeto sitio |
| /api/cooperativas | GET | Obtiene todos los objetos cooperativas |
| /api/cooperativa/{id}| GET | Obtiene un solo objeto cooperativa |
| /api/clases | GET | Obtiene todos los objetos clases |
| /api/unidades | GET | Obtiene solo objetos del usuario logueado, Obtiene todos los objetos si es usuario administrador |
| /api/unidad/{id} | GET | Obtiene un solo objeto unidad |
| /api/pasaje | POST | Crea un objeto pasaje |
| /api/pasajes | GET | Obtiene todos los objetos pasajes |
| /api/pasajes/:fecha/:origen/:destino | GET | Obtiene todos los objetos pasajes (fecha, origen y destino) |
| /api/pasaje/{id} | GET | Obtiene un solo objeto pasaje |
| /api/pasaje/{id_pasaje} | PUT | Actualiza un objeto pasaje |
| /api/boleto | POST | Crea un objeto boleto |
| /api/boletos | GET | Obtiene todos los objetos boletos que registre el usuario logueado |
| /api/boleto/{id_boleto} | GET | Obtiene un solo objeto boleto |
| /api/boleto/{id_boleto} | DELETE | Elimina un objeto boleto |