"""empty message

Revision ID: ee2579eb99d2
Revises: 817973214c5e
Create Date: 2025-01-02 17:34:51.634855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee2579eb99d2'
down_revision: Union[str, None] = '817973214c5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mbtis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mbtis_id'), 'mbtis', ['id'], unique=False)
    op.create_index(op.f('ix_mbtis_name'), 'mbtis', ['name'], unique=False)
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('sqe', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_questions_id'), 'questions', ['id'], unique=False)
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('mbti_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('survival_percent', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['mbti_id'], ['mbtis.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_characters_id'), 'characters', ['id'], unique=False)
    op.create_index(op.f('ix_characters_name'), 'characters', ['name'], unique=False)
    op.create_table('options',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('mbti_type', sa.String(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_options_id'), 'options', ['id'], unique=False)
    op.create_table('character_mbti',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('mbti_type_id', sa.Integer(), nullable=True),
    sa.Column('e_percent', sa.Integer(), nullable=True),
    sa.Column('i_percent', sa.Integer(), nullable=True),
    sa.Column('s_percent', sa.Integer(), nullable=True),
    sa.Column('n_percent', sa.Integer(), nullable=True),
    sa.Column('t_percent', sa.Integer(), nullable=True),
    sa.Column('f_percent', sa.Integer(), nullable=True),
    sa.Column('j_percent', sa.Integer(), nullable=True),
    sa.Column('p_percent', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['mbti_type_id'], ['mbtis.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_character_mbti_id'), 'character_mbti', ['id'], unique=False)
    op.create_table('user_responses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('option_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['option_id'], ['options.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_responses_id'), 'user_responses', ['id'], unique=False)
    op.create_index(op.f('ix_user_responses_user_id'), 'user_responses', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_responses_user_id'), table_name='user_responses')
    op.drop_index(op.f('ix_user_responses_id'), table_name='user_responses')
    op.drop_table('user_responses')
    op.drop_index(op.f('ix_character_mbti_id'), table_name='character_mbti')
    op.drop_table('character_mbti')
    op.drop_index(op.f('ix_options_id'), table_name='options')
    op.drop_table('options')
    op.drop_index(op.f('ix_characters_name'), table_name='characters')
    op.drop_index(op.f('ix_characters_id'), table_name='characters')
    op.drop_table('characters')
    op.drop_index(op.f('ix_questions_id'), table_name='questions')
    op.drop_table('questions')
    op.drop_index(op.f('ix_mbtis_name'), table_name='mbtis')
    op.drop_index(op.f('ix_mbtis_id'), table_name='mbtis')
    op.drop_table('mbtis')
    # ### end Alembic commands ###