"""empty message

Revision ID: 13f5829a6ce0
Revises: 
Create Date: 2023-01-31 19:17:03.313967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13f5829a6ce0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('lastname'),
    sa.UniqueConstraint('name')
    )
    op.create_table('web',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('branding',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=100), nullable=False),
    sa.Column('logo', sa.String(length=200), nullable=False),
    sa.Column('logo_favicon', sa.String(length=200), nullable=False),
    sa.Column('font', sa.String(length=200), nullable=False),
    sa.Column('brand_name', sa.String(length=100), nullable=False),
    sa.Column('web_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['web_id'], ['web.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('brand_name'),
    sa.UniqueConstraint('logo'),
    sa.UniqueConstraint('logo_favicon')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('web_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['web_id'], ['web.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('header', sa.String(length=200), nullable=False),
    sa.Column('web_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['web_id'], ['web.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('header')
    )
    op.create_table('food',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('web_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['web_id'], ['web.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('food')
    op.drop_table('content')
    op.drop_table('category')
    op.drop_table('branding')
    op.drop_table('web')
    op.drop_table('user')
    # ### end Alembic commands ###
