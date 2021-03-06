import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'bcrypt',
    'docutils',
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_redis_sessions',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'paste',
    'redis-server',
    'waitress',
    'psycopg2==2.7.5',
    'alembic',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest >= 3.7.4',
    'pytest-cov',
    'pyramid_ipython',
]

setup(
    name='pasajes',
    version='0.0.1',
    description='pasajes',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='mricharleon',
    author_email='mricharleon@gmail.com',
    url='https://pasajes-backend.herokuapp.com/',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = pasajes:main',
        ],
        'console_scripts': [
            'initialize_pasajes_db=pasajes.scripts.initialize_db:main',
        ],
    },
)
