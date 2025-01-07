# app/domains/mbti/questions.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class MBTI(Base):
    __tablename__ = "mbtis"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    characters = relationship("Character", back_populates="mbti")
    character_mbti = relationship("CharacterMBTI", back_populates="mbti_type")


class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mbti_id = Column(Integer, ForeignKey("mbtis.id"))
    description = Column(String)
    survival_percent = Column(Integer)
    image_url = Column(String)

    mbti = relationship("MBTI", back_populates="characters")
    mbti_elements = relationship("CharacterMBTI", back_populates="character")


class CharacterMBTI(Base):
    __tablename__ = "character_mbti"
    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"))
    mbti_type_id = Column(Integer, ForeignKey("mbtis.id"))

    e_percent = Column(Integer, default=20)
    i_percent = Column(Integer, default=20)
    s_percent = Column(Integer, default=20)
    n_percent = Column(Integer, default=20)
    t_percent = Column(Integer, default=20)
    f_percent = Column(Integer, default=20)
    j_percent = Column(Integer, default=20)
    p_percent = Column(Integer, default=20)

    character = relationship("Character", back_populates="mbti_elements")
    mbti_type = relationship("MBTI", back_populates="character_mbti")

