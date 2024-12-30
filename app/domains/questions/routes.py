# app/domains/questions/routes.py
from fastapi import APIRouter, HTTPException, Form, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from app.domains.questions.services import save_user_response, get_next_question, get_question_by_id
from app.database import get_db
from sqlalchemy.orm import Session
from app.utils.common import templates
from app.domains.user.services import get_user_id_by_session

router = APIRouter()

@router.get("/question/{question_id}/{session_id}", response_class=HTMLResponse)
async def get_question(request: Request, question_id: int, session_id: str, db: Session = Depends(get_db)):
    # 세션 ID로 사용자 ID 가져오기
    user_id = get_user_id_by_session(session_id)
    if not user_id:
        raise HTTPException(status_code=401, detail="세션이 유효하지 않습니다.")

    # 서비스에서 질문 가져오기
    question = get_question_by_id(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="질문을 찾을 수 없습니다.")

    # 템플릿 렌더링
    return templates.TemplateResponse("question.html", {
        "request": request,
        "question": question,
        "question_id": question.id,
        "session_id": session_id
    })

@router.post("/question/{question_id}/{session_id}", response_class=HTMLResponse)
async def post_answer(request: Request, question_id: int, session_id: str, answer: int = Form(...), db: Session = Depends(get_db)):
    # 세션 ID로 사용자 ID 가져오기
    user_id = get_user_id_by_session(session_id)
    if not user_id:
        raise HTTPException(status_code=401, detail="세션이 유효하지 않습니다.")

    # 사용자 응답 저장
    save_user_response(db, user_id, question_id, answer)

    # 다음 질문 가져오기
    next_question = get_next_question(db, question_id)
    if not next_question:
        return RedirectResponse(url=f"/waiting/{session_id}", status_code=303)

    # 템플릿 렌더링
    return templates.TemplateResponse("question.html", {
        "request": request,
        "question": next_question,
        "question_id": next_question.id,
        "session_id": session_id
    })


#대기 화면
@router.get("/waiting/{session_id}", response_class=HTMLResponse)
async def waiting_screen(request: Request, session_id: str):
    return templates.TemplateResponse("waiting.html", {"request": request, "session_id": session_id})