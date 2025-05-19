import streamlit as st
import pandas as pd

# 대학 정보
universities = [
    {
        "name": "서울대학교",
        "lat": 37.4602,
        "lon": 126.9527,
        "desc": "대한민국 최고의 종합대학, 관악산 자락에 위치한 국립대학입니다.",

    },
    {
        "name": "연세대학교",
        "lat": 37.5658,
        "lon": 126.9386,
        "desc": "신촌 캠퍼스를 중심으로 국내 최상위권의 사립 명문 대학입니다.",
    },
    {
        "name": "고려대학교",
        "lat": 37.5915,
        "lon": 127.0364,
        "desc": "성북구 안암동에 위치한 전통과 역사를 지닌 사립 명문 대학입니다.",

    },
    {
        "name": "한양대학교",
        "lat": 37.5575,
        "lon": 127.0459,
        "desc": "서울 동쪽에 위치한 공학계열 강세의 실용 중심 대학입니다.",

    },
    {
        "name": "성균관대학교",
        "lat": 37.5874,
        "lon": 126.9936,
        "desc": "조선시대 성균관에서 유래한 전통 있는 이공계 중심 명문 대학입니다.",

    },
]

# Streamlit 설정
st.set_page_config(page_title="대학 지도 선택기", page_icon="🎓")

st.title("🎓 수도권 대학 지도 & 캠퍼스 보기")
st.markdown("원하는 대학을 선택하면 위치와 캠퍼스 모습을 보여드릴게요!")

# 대학 이름 목록
univ_names = [u["name"] for u in universities]

# 드롭다운으로 대학 선택
selected_name = st.selectbox("🏫 대학을 선택하세요:", univ_names)

# 선택된 대학 데이터 가져오기
selected_univ = next(u for u in universities if u["name"] == selected_name)

# 지도 표시
st.subheader(f"📍 {selected_univ['name']} 위치")
map_df = pd.DataFrame([[selected_univ["lat"], selected_univ["lon"]]], columns=["lat", "lon"])
st.map(map_df, zoom=15)

# 설명 출력


st.subheader("📝 대학 소개")
st.markdown(selected_univ["desc"])
