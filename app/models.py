from app.domains.user import models as user_models
from app.domains.questions import models as questions_models
from app.domains.mbti import models as mbti_models

# # app/models.py
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
#
#
# Base = declarative_base()
#
# # Character 모델
# class Character(Base):
#     __tablename__ = "characters"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     mbti_id = Column(Integer, ForeignKey("mbtis.id"))
#     description = Column(String)
#     survival_percent = Column(Integer)
#     image_url = Column(String)
#
#     mbti = relationship("MBTI", back_populates="characters")
#     mbti_elements = relationship("CharacterMBTI", back_populates="character")
#
# class CharacterMBTI(Base):
#     __tablename__ = "character_mbti"
#     id = Column(Integer, primary_key=True, index=True)
#     character_id = Column(Integer, ForeignKey("characters.id"))
#     mbti_type_id = Column(Integer, ForeignKey("mbtis.id"))
#
#     e_percent = Column(Integer, default=20)
#     i_percent = Column(Integer, default=20)
#     s_percent = Column(Integer, default=20)
#     n_percent = Column(Integer, default=20)
#     t_percent = Column(Integer, default=20)
#     f_percent = Column(Integer, default=20)
#     j_percent = Column(Integer, default=20)
#     p_percent = Column(Integer, default=20)
#
#     character = relationship("Character", back_populates="mbti_elements")
#     mbti_type = relationship("MBTI", back_populates="character_mbti")
#
# class MBTI(Base):
#     __tablename__ = "mbtis"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#
#     characters = relationship("Character", back_populates="mbti")
#     character_mbti = relationship("CharacterMBTI", back_populates="mbti_type")
#
# class Question(Base):
#     __tablename__ = "questions"
#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String)
#
#     options = relationship("Option", back_populates="question")
#     responses = relationship("UserResponse", back_populates="question")
#
# class Option(Base):
#     __tablename__ = "options"
#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String)
#     mbti_type = Column(String)
#     score = Column(Integer)
#
#     question_id = Column(Integer, ForeignKey("questions.id"))
#     question = relationship("Question", back_populates="options")
#
# # class Result(Base):
# #     __tablename__ = "results"
# #     id = Column(Integer, primary_key=True, index=True)
# #     user_id = Column(Integer)
# #     mbti_type = Column(String)
# #     description = Column(String)
# #     survival_percent = Column(Integer)
# #     character_id = Column(Integer, ForeignKey("characters.id"))
# #
# #     character = relationship("Character")
#
# class UserResponse(Base):
#     __tablename__ = "user_responses"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, index=True)
#     question_id = Column(Integer, ForeignKey("questions.id"))
#     option_id = Column(Integer, ForeignKey('options.id'))
#
#     question = relationship("Question", back_populates="responses")
#     option = relationship("Option")
