import streamlit as st
from datetime import datetime, timedelta

def get_starttime():
    if 'cur_time' not in st.session_state:
        st.session_state.cur_time = datetime.now().time()

    cols = st.columns(2)
    with cols[0]:
        # 첫번째 대기자 시작 시간 입력 (기본값은 현재 시간)
        start_time = st.time_input("첫번째 대기자 시작 시간", step=60)
    with cols[1]:    
        # 더할 분 B 입력
        waiting = st.number_input("대기 순서", min_value=0, value=50, step=1)

    # 오늘 짜와 입력된 시간을 조합하여 datetime 객체 생성 (날짜 변경선 처리를 위함)
    today = datetime.today()
    base_datetime = datetime.combine(today, start_time)

    # 시간 계산 (B분 더하기)
    result_datetime = base_datetime + timedelta(minutes=(50+waiting-1)*5)

    # 결과 출력
    # 결과 시간이 다음 날로 넘어갔는지 확인
    if result_datetime.date() > today.date():
        st.info(f"**익일(다음날) {result_datetime.strftime('%H시 %M분')}** 입니다.")
    else:
        st.info(f"오늘 **{result_datetime.strftime('%H시 %M분')}** 입니다.")
