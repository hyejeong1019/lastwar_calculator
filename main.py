import streamlit as st
from lawar_time import get_starttime
from lawar_score import get_acc_scores

# 1. 앱 상단에 이 CSS 코드를 한 번만 주입해 줍니다.
st.markdown("""
    <style>
    /* 1) 익스팬더 헤더 전체 글자 크기 및 두께 조정 */
    .stExpander details summary p {
        font-size: 20px !important;
        font-weight: bold !important;
    }
    /* 2) 익스팬더 토글 화살표 크기도 글자 크기에 맞춰 조정 (선택사항) */
    .stExpander details summary svg {
        width: 20px !important;
        height: 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

def get_large_label(label):
    return f'<span style="font-size: 22px; font-weight: bold; color: #1E88E5;">{label}</span>'

# 페이지 제목 설정
st.title("🕒 Last War 계산기")
with st.expander("장관/부장 시간 계산"):
    st.markdown("**대기가 50명이 넘는 경우 시간 계산**")
    get_starttime()
with st.expander("가속 점수 계산"):
    st.markdown('가속 적용 시간에 대한 군비 또는 연대 점수 계산')
    get_acc_scores()
   