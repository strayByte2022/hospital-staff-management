"""initial

Revision ID: 2fea24b8bd13
Revises: 
Create Date: 2025-04-10 00:13:39.902070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fea24b8bd13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('staff',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('StaffId', sa.Integer(), nullable=True),
    sa.Column('Name', sa.Text(), nullable=True),
    sa.Column('Role', sa.Text(), nullable=True),
    sa.Column('Speciality', sa.Text(), nullable=True),
    sa.Column('Contact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('doctor',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('StaffId', sa.Integer(), nullable=True),
    sa.Column('LicenseNumber', sa.Text(), nullable=True),
    sa.Column('ColumnName', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['StaffId'], ['staff.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('nurse',
    sa.Column('Id', sa.Integer(), nullable=True),
    sa.Column('StaffId', sa.Integer(), nullable=True),
    sa.Column('Certification', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['StaffId'], ['staff.Id'], )
    )
    op.create_table('schedule',
    sa.Column('Id', sa.Integer(), nullable=True),
    sa.Column('StaffId', sa.Integer(), nullable=True),
    sa.Column('Description', sa.Text(), nullable=True),
    sa.Column('Created', sa.Text(), nullable=True),
    sa.Column('Updated', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['StaffId'], ['staff.Id'], )
    )
    op.create_table('shift',
    sa.Column('Id', sa.Integer(), nullable=True),
    sa.Column('StartTime', sa.Text(), nullable=True),
    sa.Column('EndTime', sa.Text(), nullable=True),
    sa.Column('Created', sa.Text(), nullable=True),
    sa.Column('Updated', sa.Text(), nullable=True),
    sa.Column('ScheduleId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ScheduleId'], ['schedule.Id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shift')
    op.drop_table('schedule')
    op.drop_table('nurse')
    op.drop_table('doctor')
    op.drop_table('staff')
    # ### end Alembic commands ###
