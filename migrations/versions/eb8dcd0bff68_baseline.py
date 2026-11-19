"""baseline

Revision ID: eb8dcd0bff68
Revises:
Create Date: 2026-11-19 23:02:58.349890

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "eb8dcd0bff68"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
