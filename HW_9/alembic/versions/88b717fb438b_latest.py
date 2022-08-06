"""'Latest'

Revision ID: 88b717fb438b
Revises: 935b7d7bbb11
Create Date: 2022-08-06 20:09:02.212067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88b717fb438b'
down_revision = '935b7d7bbb11'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('con_phon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contact', sa.Integer(), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contact'], ['contact.id'], ),
    sa.ForeignKeyConstraint(['phone'], ['phones.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('con_phon')
    # ### end Alembic commands ###