"""alter task completed column to boolean

Revision ID: 291a5f4397cf
Revises: 8593a43093aa
Create Date: 2023-04-09 20:34:40.042433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '291a5f4397cf'
down_revision = '8593a43093aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task_category')
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('category_id')

    with op.batch_alter_table('task_tag', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['task_id', 'tag_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task_tag', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key(None, 'category', ['category_id'], ['id'])

    op.create_table('task_category',
    sa.Column('task_id', sa.INTEGER(), nullable=False),
    sa.Column('category_id', sa.INTEGER(), nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.PrimaryKeyConstraint('task_id', 'category_id', 'id')
    )
    # ### end Alembic commands ###
