from sqlalchemy.orm import Session
from app.domains.mbti.mbti import MBTI, Character

def get_all_mbti_types(db: Session):
    return db.query(MBTI).all()

def get_character_by_mbti_type(db: Session, mbti_id: int):
    return db.query(Character).filter(Character.mbti_id == mbti_id).all()
