"""empty message

Revision ID: efcc8007ecba
Revises: 5579cddcde29
Create Date: 2021-12-01 12:00:10.481514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efcc8007ecba'
down_revision = '5579cddcde29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'favorite', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'favorite', type_='unique')
    # ### end Alembic commands ###
