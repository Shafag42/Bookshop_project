"""empty message

Revision ID: 6e790afe5c07
Revises: c93f5e5b220d
Create Date: 2022-05-20 12:04:25.247943

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6e790afe5c07'
down_revision = 'c93f5e5b220d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=30), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('date_of_comment', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.alter_column('books', 'title',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               nullable=True)
    op.alter_column('books', 'author',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.alter_column('books', 'description',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)
    op.alter_column('books', 'stock',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('books', 'genre',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('books', 'language_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.create_unique_constraint(None, 'books', ['title'])
    op.drop_column('books', 'updated_at')
    op.drop_column('books', 'created_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('created_at', mysql.DATETIME(), nullable=True))
    op.add_column('books', sa.Column('updated_at', mysql.DATETIME(), nullable=True))
    op.drop_constraint(None, 'books', type_='unique')
    op.alter_column('books', 'language_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('books', 'genre',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('books', 'stock',
               existing_type=sa.Integer(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('books', 'description',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=True)
    op.alter_column('books', 'author',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
    op.alter_column('books', 'title',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               nullable=False)
    op.drop_table('user')
    op.drop_table('Comments')
    # ### end Alembic commands ###