"""Alter repo labor unique

Revision ID: 24
Revises: 23
Create Date: 2023-08-25 18:17:22.651191

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text
import re

# revision identifiers, used by Alembic.
revision = '24'
down_revision = '23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    conn = op.get_bind()

    #Remove constraint being initially deferred.
    conn.execute(text(f"""
    ALTER TABLE "augur_data"."repo_labor" 
        DROP CONSTRAINT IF EXISTS "rl-unique",
        ADD CONSTRAINT "rl-unique" UNIQUE ("repo_id", "rl_analysis_date", "file_path", "file_name");
    """))
    """
    
    """
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()

    #Make unique initially deferred
    conn.execute(text(f"""
    ALTER TABLE "augur_data"."repo_labor" 
        DROP CONSTRAINT IF EXISTS "rl-unique",
        ADD CONSTRAINT "rl-unique" UNIQUE ("repo_id", "rl_analysis_date", "file_path", "file_name") DEFERRABLE INITIALLY DEFERRED;
    """))

    # ### end Alembic commands ###
