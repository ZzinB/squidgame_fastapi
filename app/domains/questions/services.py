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

# 다음 문제 가져오기
def get_next_question(db: Session, current_question_id: int):
    # next_question = db.query(question_models.Question).filter(question_models.Question.id == current_question_id + 1).first()
    next_question = db.query(question_models.Question).filter(question_models.Question.id > current_question_id).order_by(question_models.Question.id).first()

    # print(f"Next question for {current_question_id}: {next_question.id if next_question else 'None'}")
    return next_question


# 특정 문제 ID로 문제 가져오기
def get_question_by_id(db: Session, question_id: int):
    id_question = db.query(question_models.Question).filter(question_models.Question.id == question_id).first()
    print(f"get_question_by_id returned: {id_question}")
    return id_question


# 첫 번째 문제 가져오기
def get_first_question(db: Session):
    return db.query(question_models.Question).order_by(question_models.Question.id).first()
