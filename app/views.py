# app/views.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db  # get_db를 임포트
import models

class QuestionView:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/questions", self.get_questions, methods=["GET"])

    async def get_questions(self, db: Session = Depends(get_db)):  # get_db 의존성 사용
        questions = db.query(models.Question).all()
        return questions  # Schema 변환 추가 가능


question_view = QuestionView()
