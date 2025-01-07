from app.models import questions, user
from sqlalchemy.orm import Session

# 사용자가 선택한 답변 저장
def save_user_response(db: Session, user_id: str, question_id: int, answer: int):
    if isinstance(user_id, dict):
        user_id = user_id.get('user_id', None)  # 'user_id' 키의 값 추출

    existing_response = db.query(user.UserResponse).filter(
        user.UserResponse.user_id == user_id,
        user.UserResponse.question_id == question_id
    ).first()

    if existing_response:
        # 기존 답변이 있으면 기존 답변을 업데이트
        existing_response.option_id = answer
    else:
        user_response = user.UserResponse(
            user_id=user_id,
            question_id=question_id,
            option_id=answer
        )
        db.add(user_response)
    db.commit()


# 다음 문제 가져오기
def get_next_question(db: Session, current_question_id: int):
    next_question = db.query(questions.Question).filter(questions.Question.id > current_question_id).order_by(questions.Question.id).first()
    return next_question


# 특정 문제 ID로 문제 가져오기
def get_question_by_id(db: Session, question_id: int):
    id_question = db.query(questions.Question).filter(questions.Question.id == question_id).first()
    return id_question


# 첫 번째 문제 가져오기
def get_first_question(db: Session):
    return db.query(questions.Question).order_by(questions.Question.id).first()

