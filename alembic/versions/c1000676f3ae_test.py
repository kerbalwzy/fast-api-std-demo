"""test

Revision ID: c1000676f3ae
Revises: dd5bb39a72cd
Create Date: 2022-02-28 20:43:15.895851

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c1000676f3ae'
down_revision = 'dd5bb39a72cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('create_at', mysql.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('update_at', mysql.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('delete_at', mysql.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('account', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('password', mysql.TEXT(), nullable=True),
    sa.Column('avatar', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
