"""add login information

Revision ID: 8824e5ad7a2d
Revises: 805bfa594720
Create Date: 2017-09-07 21:45:45.138797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8824e5ad7a2d'
down_revision = '805bfa594720'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###