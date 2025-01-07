from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.user import UserResponse
from app.database import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    sqe = Column(Integer, default=1)

    options = relationship("Option", back_populates="question")
    responses = relationship("UserResponse", back_populates="question")

class Option(Base):
    __tablename__ = "options"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    mbti_type = Column(String)
    score = Column(Integer)

    question_id = Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", back_populates="options")
