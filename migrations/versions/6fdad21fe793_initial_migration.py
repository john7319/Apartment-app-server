"""Initial Migration

Revision ID: 6fdad21fe793
Revises: 
Create Date: 2024-08-29 15:24:50.542723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fdad21fe793'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('token_verified', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('apartments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('house_no', sa.String(), nullable=False),
    sa.Column('water_bill', sa.Integer(), nullable=True),
    sa.Column('electric_bill', sa.Integer(), nullable=True),
    sa.Column('trash_bill', sa.Integer(), nullable=True),
    sa.Column('security_bill', sa.Integer(), nullable=True),
    sa.Column('rent', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('report', sa.String(), nullable=False),
    sa.Column('status_report', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_apartments_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lease_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('apartment_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['apartment_id'], ['apartments.id'], name=op.f('fk_lease_history_apartment_id_apartments')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_lease_history_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('leases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('apartment_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['apartment_id'], ['apartments.id'], name=op.f('fk_leases_apartment_id_apartments')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_leases_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leases')
    op.drop_table('lease_history')
    op.drop_table('apartments')
    op.drop_table('users')
    # ### end Alembic commands ###
