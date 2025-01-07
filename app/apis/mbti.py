# app/domains/mbti/questions.py
from sqlalchemy.orm import Session
from app.models import questions, user

# 사용자 응답에 기반한 MBTI 결과 계산
def calculate_mbti_result(db: Session, user_id: str):
    responses = db.query(user.UserResponse).filter(user.UserResponse.user_id == user_id).all()

    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

    for response in responses:
        selected_option = db.query(questions.Option).filter(questions.Option.id == response.option_id).first()
        if selected_option:
            scores[selected_option.mbti_type] += selected_option.score

    mbti_type = f"{'E' if scores['E'] > scores['I'] else 'I'}" \
                f"{'S' if scores['S'] > scores['N'] else 'N'}" \
                f"{'T' if scores['T'] > scores['F'] else 'F'}" \
                f"{'J' if scores['J'] > scores['P'] else 'P'}"

    return mbti_type, scores

# MBTI 점수와 캐릭터 간의 매칭 점수 계산
def calculate_match_score(scores, character):
    # 예시: 점수 계산 로직을 구현
    match_score = 0
    match_score += abs(scores['E'] - character.mbti_elements[0].e_percent)
    match_score += abs(scores['I'] - character.mbti_elements[0].i_percent)
    match_score += abs(scores['S'] - character.mbti_elements[0].s_percent)
    match_score += abs(scores['N'] - character.mbti_elements[0].n_percent)
    match_score += abs(scores['T'] - character.mbti_elements[0].t_percent)
    match_score += abs(scores['F'] - character.mbti_elements[0].f_percent)
    match_score += abs(scores['J'] - character.mbti_elements[0].j_percent)
    match_score += abs(scores['P'] - character.mbti_elements[0].p_percent)
    return match_score
