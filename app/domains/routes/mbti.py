from fastapi import APIRouter, HTTPException, Depends
from app.domains.mbti.mbti import calculate_mbti_result, calculate_match_score
from app.database import get_db
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi import Request
from app.domains.mbti import mbti
from app.utils.common import templates
from app.domains.user.user import get_user_id_by_session

router = APIRouter()

@router.get("/result/{session_id}", response_class=HTMLResponse)
async def calculate_result(request: Request, session_id: str, db: Session = Depends(get_db)):
    user_data = get_user_id_by_session(session_id)
    if not user_data:
        raise HTTPException(status_code=401, detail="세션이 유효하지 않습니다.")

    user_id = user_data
    if not user_id:
        raise HTTPException(status_code=401, detail="사용자 ID가 존재하지 않습니다.")

    # MBTI 계산 로직
    mbti_type, scores = calculate_mbti_result(db, user_id)

    characters = db.query(models.Character).join(models.MBTI).filter(models.MBTI.name == mbti_type).all()
    if characters:
        best_character = min(characters, key=lambda character: calculate_match_score(scores, character))
        return templates.TemplateResponse("result.html", {
            "request": request,
            "mbti_type": mbti_type,
            "character_name": best_character.name,
            "mbti_description": best_character.description,
            "survival_percent": best_character.survival_percent,
            "character_image_url": best_character.image_url,
        })

    return templates.TemplateResponse("result.html", {
        "request": request,
        "mbti_type": "알 수 없음",
        "character_name": "알 수 없음",
        "mbti_description": "설명이 없습니다.",
        "survival_percent": "알 수 없음",
        "character_image_url": "/static/default.jpg",
    })