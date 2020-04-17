"""init

Revision ID: 9ad19b261893
Revises: 
Create Date: 2020-03-26 11:24:19.292259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ad19b261893'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_clases')),
    sa.UniqueConstraint('nombre', name=op.f('uq_clases_nombre'))
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_roles')),
    sa.UniqueConstraint('nombre', name=op.f('uq_roles_nombre'))
    )
    op.create_table('sitios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ciudad', sa.Text(), nullable=False),
    sa.Column('terminal', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_sitios'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('role', sa.Text(), nullable=False),
    sa.Column('password_hash', sa.Text(), nullable=True),
    sa.Column('rol_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['rol_id'], ['roles.id'], name=op.f('fk_users_rol_id_roles')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('name', name=op.f('uq_users_name'))
    )
    op.create_table('cooperativas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_cooperativas_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cooperativas')),
    sa.UniqueConstraint('nombre', name=op.f('uq_cooperativas_nombre'))
    )
    op.create_table('pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('data', sa.Text(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], name=op.f('fk_pages_creator_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_pages')),
    sa.UniqueConstraint('name', name=op.f('uq_pages_name'))
    )
    op.create_table('unidades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero_asientos', sa.Integer(), nullable=False),
    sa.Column('numero_unidad', sa.Integer(), nullable=False),
    sa.Column('clase_id', sa.Integer(), nullable=False),
    sa.Column('cooperativa_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['clase_id'], ['clases.id'], name=op.f('fk_unidades_clase_id_clases')),
    sa.ForeignKeyConstraint(['cooperativa_id'], ['cooperativas.id'], name=op.f('fk_unidades_cooperativa_id_cooperativas')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_unidades'))
    )
    op.create_table('pasajes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('salida', sa.DateTime(), nullable=True),
    sa.Column('llegada', sa.DateTime(), nullable=True),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('asientos_disponibles', sa.Integer(), nullable=False),
    sa.Column('origen_sitio_id', sa.Integer(), nullable=False),
    sa.Column('destino_sitio_id', sa.Integer(), nullable=False),
    sa.Column('unidad_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['destino_sitio_id'], ['sitios.id'], name=op.f('fk_pasajes_destino_sitio_id_sitios')),
    sa.ForeignKeyConstraint(['origen_sitio_id'], ['sitios.id'], name=op.f('fk_pasajes_origen_sitio_id_sitios')),
    sa.ForeignKeyConstraint(['unidad_id'], ['unidades.id'], name=op.f('fk_pasajes_unidad_id_unidades')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_pasajes'))
    )
    op.create_table('boletos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero_asientos', sa.Integer(), nullable=False),
    sa.Column('precio_total', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pasaje_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pasaje_id'], ['pasajes.id'], name=op.f('fk_boletos_pasaje_id_pasajes')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_boletos_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_boletos'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('boletos')
    op.drop_table('pasajes')
    op.drop_table('unidades')
    op.drop_table('pages')
    op.drop_table('cooperativas')
    op.drop_table('users')
    op.drop_table('sitios')
    op.drop_table('roles')
    op.drop_table('clases')
    # ### end Alembic commands ###
