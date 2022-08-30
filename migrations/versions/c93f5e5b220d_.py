"""empty message

Revision ID: c93f5e5b220d
Revises: df4133e9f4bf
Create Date: 2022-05-17 12:45:51.460255

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c93f5e5b220d'
down_revision = 'df4133e9f4bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Language',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lang_code', sa.String(length=2), nullable=False),
    sa.Column('lang_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('genre')
    op.drop_table('language')
    op.add_column('books', sa.Column('genre_id', sa.Integer(), nullable=True))
    op.alter_column('books', 'stock',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Integer(),
               existing_nullable=True)
    op.drop_constraint('books_ibfk_1', 'books', type_='foreignkey')
    op.drop_constraint('books_ibfk_2', 'books', type_='foreignkey')
    op.create_foreign_key(None, 'books', 'Language', ['language_id'], ['id'])
    op.create_foreign_key(None, 'books', 'Genre', ['genre_id'], ['id'])
    op.drop_column('books', 'genre')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('genre', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.create_foreign_key('books_ibfk_2', 'books', 'language', ['language_id'], ['id'])
    op.create_foreign_key('books_ibfk_1', 'books', 'genre', ['genre'], ['id'])
    op.alter_column('books', 'stock',
               existing_type=sa.Integer(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.drop_column('books', 'genre_id')
    op.create_table('language',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('lang_code', mysql.VARCHAR(length=2), nullable=False),
    sa.Column('lang_name', mysql.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('genre',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('Language')
    op.drop_table('Genre')
    # ### end Alembic commands ###