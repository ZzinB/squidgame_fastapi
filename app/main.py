# app/main.py
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from app.domains.questions.routes import router as questions_router
from app.domains.mbti.routes import router as mbti_router
from app.domains.user.routes import router as user_router


# 공통 설정
#templates = Jinja2Templates(directory="app/templates")

# FastAPI 애플리케이션 초기화
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 라우터 등록
app.include_router(questions_router)
app.include_router(mbti_router)  # MBTI 관련 라우터 등록
app.include_router(user_router)  # 사용자 관련 라우터 등록


# from fastapi import FastAPI, HTTPException, Depends, status, Cookie, Request, Response, Form
# from typing import Optional
# from uuid import uuid4
# from fastapi.responses import HTMLResponse, RedirectResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from sqlalchemy.orm import Session
# from app.database import get_db
# from app import models
#
# app = FastAPI()
#
# # static 파일 서빙
# app.mount("/static", StaticFiles(directory="app/static"), name="static")
# # Jinja2Templates 인스턴스 생성
# templates = Jinja2Templates(directory="app/templates")
#
# # 세션 데이터를 저장할 딕셔너리(임시)
# session_data = {}
#
#
# # 세션 ID를 생성하는 함수
# def generate_session_id():
#     return str(uuid4())
#
#
# # 사용자 ID 생성 (임시로 UUID 사용하여 고유 ID 생성)
# def generate_user_id():
#     return str(uuid4())  # 고유한 사용자 ID 생성
#
#
# # 홈 화면 (시작 버튼이 있는 화면)
# @app.get("/", response_class=HTMLResponse)
# async def index(request: Request, response: Response, session_id: Optional[str] = Cookie(None)):
#     # 세션 ID가 없으면 새로 생성하여 쿠키에 저장
#     if not session_id:
#         session_id = generate_session_id()
#         cookie = f"session_id={session_id}; Path=/; HttpOnly"
#         response.set_cookie("session_id", session_id)  # 쿠키에 세션 ID 저장
#         session_data[session_id] = {"user_id": generate_user_id()}  # 임시로 user_id 저장
#
#     # 사용자 ID 추출
#     user_id = session_data.get(session_id, {}).get("user_id")
#
#     return templates.TemplateResponse("index.html", {"request": request, "user_id": user_id, "session_id": session_id})
#
#
# # 질문 화면 (각 문제에 대한 화면)
# @app.get("/question/{question_id}/{session_id}", response_class=HTMLResponse)
# async def get_question(request: Request, question_id: int, session_id: str, db: Session = Depends(get_db)):
#     # print(f"Question ID: {question_id}, Session ID: {session_id}")  # 디버깅용 출력
#
#     question = db.query(models.Question).filter(models.Question.id == question_id).first()
#
#     if question:
#         return templates.TemplateResponse("question.html", {
#             "request": request,
#             "question": question,
#             "question_id": question_id,
#             "session_id": session_id
#         })
#     else:
#         return {"error": "Question not found"}
#
#
# # 사용자가 답변을 제출했을 때 (답변 저장 후 다음 문제로 이동)
# @app.post("/question/{question_id}/{session_id}", response_class=HTMLResponse)
# async def post_answer(request: Request, question_id: int, session_id: str, answer: int = Form(...),
#                       db: Session = Depends(get_db)):
#     user_id = session_data.get(session_id, {}).get("user_id")
#     if not user_id:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="세션이 유효하지 않습니다.")
#
#     # 사용자 응답을 DB에 저장
#     user_response = models.UserResponse(user_id=user_id, question_id=question_id, option_id=answer)
#
#     try:
#         db.add(user_response)
#         db.commit()
#     except Exception as e:
#         db.rollback()  # 에러 발생 시 롤백
#         raise HTTPException(status_code=500, detail="An error occurred while saving your response.")
#
#     # 다음 문제 조회 (현재 question_id에 대해 다음 문제를 찾음)
#     next_question = db.query(models.Question).filter(models.Question.id == question_id + 1).first()
#
#     if not next_question:
#         # 결과 페이지로 리다이렉트 (GET 요청으로)
#         return RedirectResponse(url=f"/waiting/{session_id}", status_code=303)
#
#     # 다음 문제로 이동
#     return templates.TemplateResponse("question.html", {
#         "request": request,
#         "question": next_question,
#         "question_id": next_question.id,  # 템플릿에 다음 문제 ID를 전달
#         "session_id": session_id
#     })
#
#
# # 결과 화면 (사용자의 MBTI 결과를 계산하여 표시)
# @app.get("/result/{session_id}", response_class=HTMLResponse)
# async def calculate_result(request: Request, session_id: str, db: Session = Depends(get_db)):
#     user_id = session_data.get(session_id, {}).get("user_id")
#     if not user_id:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="세션이 유효하지 않습니다.")
#
#     # 사용자의 응답을 가져오기
#     responses = db.query(models.UserResponse).filter(models.UserResponse.user_id == user_id).all()
#
#     # MBTI 점수 초기화
#     scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
#
#     # 각 질문에 대한 선택지를 가져오기
#     for response in responses:
#         selected_option = db.query(models.Option).filter(models.Option.id == response.option_id).first()
#         if selected_option:
#             # 선택된 option의 mbti에 해당하는 점수를 추가
#             scores[selected_option.mbti_type] += selected_option.score
#
#     # MBTI 유형 결정
#     mbti_type = f"{'E' if scores['E'] > scores['I'] else 'I'}" \
#                 f"{'S' if scores['S'] > scores['N'] else 'N'}" \
#                 f"{'T' if scores['T'] > scores['F'] else 'F'}" \
#                 f"{'J' if scores['J'] > scores['P'] else 'P'}"
#
#     # MBTI 유형에 맞는 캐릭터들을 찾기
#     characters = db.query(models.Character).join(models.MBTI).filter(models.MBTI.name == mbti_type).all()
#
#     if characters:
#         # 가장 적합한 캐릭터를 찾기 위해 점수 계산
#         best_character = None
#         best_match_score = float('inf')
#
#         for character in characters:
#             # 각 캐릭터의 CharacterMBTI를 가져오기
#             character_mbti = db.query(models.CharacterMBTI).filter(
#                 models.CharacterMBTI.character_id == character.id).first()
#             # MBTI 특성별 점수 계산
#             match_score = 0
#             for mbti_letter, score in scores.items():
#                 if mbti_letter == "E" or mbti_letter == "I":
#                     match_score += abs(character_mbti.e_percent - score)
#                 elif mbti_letter == "S" or mbti_letter == "N":
#                     match_score += abs(character_mbti.s_percent - score)
#                 elif mbti_letter == "T" or mbti_letter == "F":
#                     match_score += abs(character_mbti.t_percent - score)
#                 elif mbti_letter == "J" or mbti_letter == "P":
#                     match_score += abs(character_mbti.j_percent - score)
#
#             # 가장 높은 점수 (가장 잘 맞는 캐릭터) 선택
#             if match_score < best_match_score:
#                 best_match_score = match_score
#                 best_character = character
#
#         if best_character:
#             character_name = best_character.name
#             mbti_description = best_character.description
#             survival_percent = best_character.survival_percent
#             character_image_url = best_character.image_url
#         else:
#             character_name = "알 수 없음"
#             mbti_description = "설명이 없습니다."
#             survival_percent = "알 수 없음"
#             character_image_url = "/static/default.jpg"
#     else:
#         character_name = "알 수 없음"
#         mbti_description = "설명이 없습니다."
#         survival_percent = "알 수 없음"
#         character_image_url = "/static/default.jpg"
#
#     # 결과 화면에 표시
#     return templates.TemplateResponse("result.html", {
#         "request": request,
#         "mbti_type": mbti_type,
#         "character_name": character_name,
#         "mbti_description": mbti_description,
#         "survival_percent": survival_percent,
#         "character_image_url": character_image_url,
#     })
#
# #대기 화면
# @app.get("/waiting/{session_id}", response_class=HTMLResponse)
# async def waiting_screen(request: Request, session_id: str):
#     return templates.TemplateResponse("waiting.html", {"request": request, "session_id": session_id})
