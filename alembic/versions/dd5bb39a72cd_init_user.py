"""init user

Revision ID: dd5bb39a72cd
Revises: 
Create Date: 2022-02-28 20:36:11.024963

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd5bb39a72cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'home_pic')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('home_pic', mysql.TEXT(), nullable=True))
    # ### end Alembic commands ###
