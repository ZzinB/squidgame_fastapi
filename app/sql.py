# app/db_utils.py
from app import database
from app.domains.mbti import models as mbti_model
from app.domains.questions import models as questions_models

def add_data_to_database():
    # 데이터베이스 세션 생성
    db = database.SessionLocal()

    # 데이터가 이미 존재하는지 확인하는 함수
    def check_if_data_exists():
        # MBTI 테이블에 데이터가 존재하는지 확인
        if db.query(mbti_model.MBTI).count() > 0:
            return True
        return False

    # 데이터가 이미 존재하지 않으면 삽입
    if not check_if_data_exists():
        try:
            # MBTI 데이터 추가
            mbtis = [
                mbti_model.MBTI(name="ISTJ"),
                mbti_model.MBTI(name="ISTP"),
                mbti_model.MBTI(name="ISFJ"),
                mbti_model.MBTI(name="ISFP"),
                mbti_model.MBTI(name="INFJ"),
                mbti_model.MBTI(name="INFP"),
                mbti_model.MBTI(name="INTJ"),
                mbti_model.MBTI(name="INTP"),
                mbti_model.MBTI(name="ESTP"),
                mbti_model.MBTI(name="ESTJ"),
                mbti_model.MBTI(name="ESFP"),
                mbti_model.MBTI(name="ESFJ"),
                mbti_model.MBTI(name="ENFP"),
                mbti_model.MBTI(name="ENFJ"),
                mbti_model.MBTI(name="ENTP"),
                mbti_model.MBTI(name="ENTJ")
            ]

            characters = [
                mbti_model.Character(name="조상우", mbti_id=7, description="218번", survival_percent=90, image_url="https://i.namu.wiki/i/dB4RR5SHzB-1CE-4WbJYX4mlm8QagNOPtxWf5pg1UZZluvVxhjSyECUFpK-zflBt-igOVeg8W85Zcz3iAVXyPg.bmp"),
                mbti_model.Character(name="강새벽", mbti_id=2, description="67번", survival_percent=80, image_url="https://i.namu.wiki/i/s0vghtnF59hyxAhFibyjpvJJe6XqyAKDCvGLCuLV4iIY6V1UxgbUM7QyTiRCU69KydCoZ_p1TK1BSVms7LoQtA.bmp"),
                mbti_model.Character(name="성기훈", mbti_id=13, description="456번", survival_percent=100, image_url="https://i.namu.wiki/i/AWE3SJiqSWXaZ2yY6-CLMsGRO43Es9vzDqPMHCL2cSjPDEjX1DLweeArHbhMnkwTmbR737QPYmFc9F5TwC6TNg.bmp"),
                mbti_model.Character(name="오일남", mbti_id=14, description="456번", survival_percent=98, image_url="https://i.namu.wiki/i/HPpKW7Y5BW-ozy0gCtqq1mz-5DvJFs8tsd_joSsI1s5jR2bsYUZVGq0Fbpl95_N_dwRrEFXaSZPSHMth-Ergbw.bmp"),
                mbti_model.Character(name="황준호", mbti_id=2, description="1번", survival_percent=99, image_url="https://i.namu.wiki/i/1G40xQNX8NwmRmmGLIBULruQ7whIXHoj6jkVp7w0jg4B-0zMg786md1Z1i7RMBbUNavjQINL9ggxy1e0j4bF_w.bmp"),
                mbti_model.Character(name="프론트맨", mbti_id=1, description="", survival_percent=100, image_url="https://i.namu.wiki/i/sbjKxKrqD32c94kExaRDHv46qnE_zTeumSIp_iutkkUsNHqCKXyuql-7j2KZzvA7v7vozkJfr-pN8a9kjGQBpJUrQyWZz8QTJ8e_jHzGiRm57KJ93o4hVzYShL5OgATtW_dPk8NjKEfCRAS5LBgz7g.webp"),
            ]

            character_mbti_data = [
                mbti_model.CharacterMBTI(character_id=1, mbti_type_id=7, e_percent=0, i_percent=51, s_percent=40, n_percent=97, t_percent=100, f_percent=0, j_percent=99, p_percent=0),
                mbti_model.CharacterMBTI(character_id=2, mbti_type_id=2, e_percent=0, i_percent=99, s_percent=95, n_percent=0, t_percent=96, f_percent=0, j_percent=0, p_percent=97),
                mbti_model.CharacterMBTI(character_id=3, mbti_type_id=13, e_percent=97, i_percent=0, s_percent=89,n_percent=0, t_percent=0, f_percent=98, j_percent=0, p_percent=87),
                mbti_model.CharacterMBTI(character_id=4, mbti_type_id=14, e_percent=96, i_percent=0, s_percent=0,n_percent=68, t_percent=0, f_percent=85, j_percent=86, p_percent=0),
                mbti_model.CharacterMBTI(character_id=5, mbti_type_id=2, e_percent=0, i_percent=99, s_percent=84,n_percent=0, t_percent=87, f_percent=0, j_percent=0, p_percent=84),
                mbti_model.CharacterMBTI(character_id=6, mbti_type_id=1, e_percent=0, i_percent=94, s_percent=75,n_percent=0, t_percent=98, f_percent=0, j_percent=98, p_percent=0),

            ]

            questions = [
                questions_models.Question(text="긴박한 상황에서 나는 어떻게 행동할까?"),
                questions_models.Question(text="게임에서 이익을 얻기 위해 팀을 배신할 수 있나?"),
                questions_models.Question(text="리스크가 큰 선택을 해야한다면 어떤 기준으로 결정할까?"),
                questions_models.Question(text="팀원과의 협력이 필요한 상황에서 나는 어떤 역할을 맡는가?"),
                questions_models.Question(text="게임에서 상황이 불리할 때, 어떻게 대처할 것인가?"),
                questions_models.Question(text="불공정한 게임 규칙을 발견했을 때 나는 어떻게 행동할까?"),
                questions_models.Question(text="승리가 눈앞에 있는 상황에서 누군가를 희생시켜야 한다면?")
            ]

            options = [
                # 첫 번째 질문에 대한 선택지
                questions_models.Option(text="침착하게 상황을 분석한다", mbti_type="E", score=1, question_id=1),
                questions_models.Option(text="본능적으로 빠르게 반응한다", mbti_type="I", score=0, question_id=1),
                questions_models.Option(text="다른 사람들과 협력해서 해결하려 한다", mbti_type="E", score=1, question_id=1),
                questions_models.Option(text="내 감정대로 행동하며 즉흥적으로 움직인다", mbti_type="I", score=0, question_id=1),

                # 두 번째 질문에 대한 선택
                questions_models.Option(text="절대 배신하지 않는다", mbti_type="J", score=1, question_id=2),
                questions_models.Option(text="필요하다면 배신할 수도 있다", mbti_type="P", score=1, question_id=2),
                questions_models.Option(text="배신은 최후의 수단으로만 고려한다", mbti_type="P", score=1, question_id=2),
                questions_models.Option(text="상황에 따라 유리한 쪽으로 움직인다", mbti_type="P", score=1, question_id=2),

                # 세 번째 질문에 대한 선택지
                questions_models.Option(text="이익을 극대화할 수 있는 선택", mbti_type="S", score=1, question_id=3),
                questions_models.Option(text="최대한 안전한 선택", mbti_type="N", score=1, question_id=3),
                questions_models.Option(text="나만 아니라 팀 전체에 이득이 되는 선택", mbti_type="S", score=1, question_id=3),
                questions_models.Option(text="직감적으로 옳다고 느껴지는 선택", mbti_type="N", score=1, question_id=3),

                # 네 번째 질문에 대한 선택지
                questions_models.Option(text="리더 역할을 맡아 팀을 이끈다", mbti_type="S", score=1, question_id=4),
                questions_models.Option(text="보조 역할을 맡아 팀원을 돕는다", mbti_type="N", score=1, question_id=4),
                questions_models.Option(text="전략을 짜는 데에 집중한다", mbti_type="S", score=1, question_id=4),
                questions_models.Option(text="모든 역할을 유연하게 맡으며 상황에 따라 행동한다", mbti_type="N", score=1, question_id=4),

                # 다섯 번째 질문에 대한 선택지
                questions_models.Option(text="침착하게 다시 전략을 짠다", mbti_type="S", score=1, question_id=5),
                questions_models.Option(text="포기하지 않고 끝까지 싸운다", mbti_type="N", score=1, question_id=5),
                questions_models.Option(text="다른 사람의 도움을 요청한다", mbti_type="S", score=1, question_id=5),
                questions_models.Option(text="상황을 모면할 방법을 즉흥적으로 찾는다", mbti_type="N", score=1, question_id=5),

                # 여섯 번째 질문에 대한 선택지
                questions_models.Option(text="조용히 규칙을 활용해서 유리하게 만든다", mbti_type="F", score=1, question_id=6),
                questions_models.Option(text="공정성을 위해 싸운다", mbti_type="F", score=1, question_id=6),
                questions_models.Option(text="팀원들에게 알려주며 협력한다", mbti_type="T", score=1, question_id=6),
                questions_models.Option(text="무시하고 나만의 방식으로 게임을 진행한다", mbti_type="T", score=1, question_id=6),

                # 일곱 번째 질문에 대한 선택지
                questions_models.Option(text="희생 없이 해결할 방법을 끝까지 찾는다", mbti_type="S", score=1, question_id=7),
                questions_models.Option(text="목적을 위해 희생을 받아들인다", mbti_type="N", score=1, question_id=7),
                questions_models.Option(text="최대한 공정한 방식으로 결정을 내린다", mbti_type="S", score=1, question_id=7),
                questions_models.Option(text="자신을 희생하더라도 다른 사람을 구하려 한다", mbti_type="N", score=1, question_id=7),
                # 다른 질문과 선택지 추가 ...
            ]

            # 데이터베이스에 추가
            db.add_all(mbtis)
            db.commit()

            db.add_all(characters)
            db.add_all(character_mbti_data)
            db.add_all(questions)
            db.add_all(options)

            db.commit()

            print("데이터가 성공적으로 추가되었습니다.")
        except Exception as e:
            db.rollback()
            print(f"Error occurred: {e}")
        finally:
            db.close()
    else:
        print("데이터가 이미 존재합니다. 추가하지 않습니다.")
