from sqlalchemy.orm import Session
from app.models.questions import Question, Option

def get_all_questions(db: Session):
    return db.query(Question).all()

def get_options_for_question(db: Session, question_id: int):
    return db.query(Option).filter(Option.question_id == question_id).all()
