# app/main.py
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from app.routes.questions import router as questions_router
from app.routes.mbti import router as mbti_router
from app.routes.user import router as user_router

# FastAPI 애플리케이션 초기화
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 라우터 등록
app.include_router(questions_router)
app.include_router(mbti_router)  # MBTI 관련 라우터 등록
app.include_router(user_router)  # 사용자 관련 라우터 등록