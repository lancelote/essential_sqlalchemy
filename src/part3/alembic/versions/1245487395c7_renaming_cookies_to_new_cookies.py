"""Renaming cookies to new_cookies

Revision ID: 1245487395c7
Revises: d0e8bc40ad9e
Create Date: 2018-03-24 20:00:38.960499

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '1245487395c7'
down_revision = 'd0e8bc40ad9e'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('cookies', 'new_cookies')


def downgrade():
    op.rename_table('new_cookies', 'cookies')
