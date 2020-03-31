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

## Usuarios
- `User:` editor  `Pass:` editor 
- `User:` basic  `Pass:` basic