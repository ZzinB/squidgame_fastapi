from fastapi import APIRouter, Request, Depends, Form, Response, Cookie
from app.database import get_db
from sqlalchemy.orm import Session
from app.apis.user import generate_session_id, create_user_session
from app.apis.questions import get_question_by_id
from fastapi.responses import HTMLResponse
from app.utils.common import templates
from typing import Optional


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, response: Response, session_id: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    if not session_id:
        session_id = generate_session_id()
        response.set_cookie("session_id", session_id)

    first_question = get_question_by_id(db, 1)

    user_id = create_user_session(session_id)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "user_id": user_id,
        "session_id": session_id,
        "first_question": first_question
    })
