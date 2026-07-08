import streamlit as st

def get_acc_scores():
    # 1. 일, 시간, 분을 가로로 깔끔하게 배치하기 위해 3컬럼 구성
    col1, col2, col3 = st.columns(3)

    with col1:
        days = st.number_input("일 (Days)", min_value=0, value=1, step=1)

    with col2:
        # 시간은 0~23시간 사이로 제한 (원하시면 max_value 제거 가능)
        hours = st.number_input("시간 (Hours)", min_value=0, max_value=23, value=12, step=1)

    with col3:
        # 분은 0~59분 사이로 제한
        minutes = st.number_input("분 (Minutes)", min_value=0, max_value=59, value=30, step=1)

    # 2. '분' 단위 환산 로직
    # 1일 = 24시간 = 1,440분
    # 1시간 = 60분
    total_minutes = (days * 24 * 60) + (hours * 60) + minutes

    st.markdown("---")

    # 3. 결과 출력 (가독성을 위해 천 단위 콤마 추가)
    st.subheader("📊 변환 결과")
    st.info(f"입력하신 시간은 총 **{total_minutes:,}분** 입니다.")

    # 시각적인 이해를 돕기 위한 추가 설명
    st.write(f"💡 세부 계산: ({days}일 × 1,440분) + ({hours}시간 × 60분) + {minutes}분")