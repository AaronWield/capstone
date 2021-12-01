"""empty message

Revision ID: 4389d1742d7b
Revises: 8daf601e6db3
Create Date: 2021-12-01 11:54:40.093298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4389d1742d7b'
down_revision = '8daf601e6db3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('duration', sa.String(length=100), nullable=True),
    sa.Column('genre', sa.String(), nullable=False),
    sa.Column('bpm', sa.String(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_table('favorite')
    # ### end Alembic commands ###