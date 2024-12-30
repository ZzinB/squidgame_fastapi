from uuid import uuid4

# 세션 ID를 생성하는 함수
def generate_session_id():
    return str(uuid4())

# 사용자 ID 생성 (임시로 UUID 사용하여 고유 ID 생성)
def generate_user_id():
    return str(uuid4())  # 고유한 사용자 ID 생성

# 사용자 세션 데이터 저장
session_data = {}

# 세션 생성 및 세션 데이터 저장
def create_user_session(session_id: str):
    if session_id not in session_data:
        user_id = generate_user_id()
        session_data[session_id] = {"user_id": user_id}
    return session_data[session_id]["user_id"]

# 세션 ID를 통한 사용자 ID 가져오기
def get_user_id_by_session(session_id: str):
    session = session_data.get(session_id)
    if session:
        return session["user_id"]
    return None
