"""add foreign-key to post table

Revision ID: 241b8bae1647
Revises: 5890603ff220
Create Date: 2023-04-14 11:56:08.002176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "241b8bae1647"
down_revision = "5890603ff220"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
