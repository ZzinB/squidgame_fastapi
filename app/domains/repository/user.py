from sqlalchemy.orm import Session
from app.domains.user.user import UserResponse

def create_user_response(db: Session, user_id: int, question_id: int, option_id: int):
    response = UserResponse(user_id=user_id, question_id=question_id, option_id=option_id)
    db.add(response)
    db.commit()
    db.refresh(response)
    return response
