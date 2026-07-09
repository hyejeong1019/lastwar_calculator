import streamlit as st

def get_acc_scores():
    # 나의 전투력, 가속, 명예훈장 점수 입력
    score_cols = st.columns([2, 1, 1])
    with score_cols[0]: #가속
        acc_score = st.number_input('가속 1분 점수', min_value=0, value=125)
        time_cols = st.columns(3)
        with time_cols[0]:
            days = st.number_input("일 (Days)", min_value=0)
        with time_cols[1]:
            # 시간은 0~23시간 사이로 제한 (원하시면 max_value 제거 가능)
            hours = st.number_input("시간 (Hours)", min_value=0, value=24)
        with time_cols[2]:
            # 분은 0~59분 사이로 제한
            minutes = st.number_input("분 (Minutes)", min_value=0)

    with score_cols[1]: #전투력
        power_score = st.number_input('전투력 1점 점수', min_value=0, value=22)
        my_power = st.number_input('전투력 상승량', min_value=0)
    with score_cols[2]: # 명예훈장
        honor_score = st.number_input('명예훈장 1점 점수', min_value=0, value=600)
        my_honor = st.number_input('명예훈장 사용 시', min_value=0)

    # 2. '분' 단위 환산 로직
    # 1일 = 24시간 = 1,440분
    # 1시간 = 60분
    total_minutes = (days * 24 * 60) + (hours * 60) + minutes

    total_scores = total_minutes * acc_score + my_power * power_score + my_honor * honor_score

    # 3. 결과 출력 (가독성을 위해 천 단위 콤마 추가)
    st.info(f"획득 예상 점수는 총 **{total_scores:,}점** 입니다.")