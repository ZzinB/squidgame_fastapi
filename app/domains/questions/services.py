from app.domains.questions import models as question_models
from app.domains.user import models as user_models
from sqlalchemy.orm import Session

# 사용자가 선택한 답변 저장
def save_user_response(db: Session, user_id: str, question_id: int, answer: int):
    if isinstance(user_id, dict):
        user_id = user_id.get('user_id', None)  # 'user_id' 키의 값 추출

    user_response = user_models.UserResponse(
        user_id=user_id,
        question_id=question_id,
        option_id=answer
    )
    db.add(user_response)
    db.commit()

# 다음 질문 찾기
def get_next_question(db: Session, current_question_id: int):
    next_question = db.query(question_models.Question).filter(question_models.Question.id == current_question_id + 1).first()
    return next_question

def get_question_by_id(db: Session, question_id: int):
    return db.query(question_models.Question).filter(question_models.Question.id == question_id).first()
