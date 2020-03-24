pasajes
=======

Getting Started
---------------

- Clonar el proyecto

    git clone git@github.com:mricharleon/pasajesBackEnd.git

- Ingresar al directorio del proyecto

    cd pasajes

- Crear un entorno virtual

    virtualenv envPasajes --python=python3

- Activar entorno virtual

    source envPasajes/bin/activate

- Actualizar herramientas

    pip install --upgrade pip setuptools

- Instalar el proyecto

    pip install -e ".[testing]"

- Configurar archivo <production.ini>

    sqlalchemy.url = postgresql://USERDB:PASSWORD@HOST:PORT/NAMEDB

- Inicializar y actualizar la base de datos usando alembic

    - Generar la primera revision

        alembic -c production.ini revision --autogenerate -m "init"

    - Actualizar 

        alembic -c production.ini upgrade head

- Cargar data por defecto 

    initialize_pasajes_db production.ini

- Ejecutar el proyecto

    pserve production.ini
