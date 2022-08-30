"""empty message

Revision ID: e93fc5e7f96d
Revises: 
Create Date: 2022-05-17 11:24:03.432126

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e93fc5e7f96d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('image_url', sa.Text(), nullable=True),
    sa.Column('stock', sa.Boolean(), nullable=True),
    sa.Column('genre', sa.String(length=40), nullable=True),
    sa.Column('language', sa.String(length=2), nullable=True),
    sa.Column('publisher', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Lang')
    op.drop_table('Book_info')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Book_info',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('author', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('published_at', sa.DATE(), nullable=True),
    sa.Column('exist', mysql.TINYINT(display_width=1), server_default=sa.text("'1'"), autoincrement=False, nullable=True),
    sa.Column('genre', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('price', mysql.DECIMAL(precision=4, scale=2), server_default=sa.text("'10.00'"), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('Lang',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('lang_code', mysql.VARCHAR(length=15), nullable=False),
    sa.Column('lang_name', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('books')
    # ### end Alembic commands ###
