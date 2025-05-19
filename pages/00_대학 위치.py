import streamlit as st
import pandas as pd

# 대학 정보 (이미지 제거, 오시는 길 추가)
universities = [
    {
        "name": "서울대학교",
        "lat": 37.4602,
        "lon": 126.9527,
        "desc": "대한민국 최고의 종합대학, 관악산 자락에 위치한 국립대학입니다.",
        "how_to_get": "지하철 2호선 서울대입구역 하차 → 5511, 5513번 버스 이용"
    },
    {
        "name": "연세대학교",
        "lat": 37.5658,
        "lon": 126.9386,
        "desc": "신촌 캠퍼스를 중심으로 국내 최상위권의 사립 명문 대학입니다.",
        "how_to_get": "지하철 2호선 신촌역 2번 출구 → 도보 10분"
    },
    {
        "name": "고려대학교",
        "lat": 37.5915,
        "lon": 127.0364,
        "desc": "성북구 안암동에 위치한 전통과 역사를 지닌 사립 명문 대학입니다.",
        "how_to_get": "지하철 6호선 안암역 2번 출구 → 도보 5분"
    },
    {
        "name": "한양대학교",
        "lat": 37.5575,
        "lon": 127.0459,
        "desc": "서울 동쪽에 위치한 공학계열 강세의 실용 중심 대학입니다.",
        "how_to_get": "지하철 2호선 한양대역 하차 → 캠퍼스 연결"
    },
    {
        "name": "성균관대학교",
        "lat": 37.5874,
        "lon": 126.9936,
        "desc": "조선시대 성균관에서 유래한 전통 있는 이공계 중심 명문 대학입니다.",
        "how_to_get": "지하철 4호선 혜화역 하차 → 도보 10분"
    },
]

# Streamlit 설정
st.set_page_config(page_title="대학 위치 및 오시는 길", page_icon="📍")

st.title("🎓 수도권 대학 지도 & 오시는 길 안내")
st.markdown("아래에서 대학을 선택하면 위치와 오시는 길 정보를 확인할 수 있어요!")

# 대학 선택
univ_names = [u["name"] for u in universities]
selected_name = st.selectbox("🏫 대학을 선택하세요:", univ_names)

# 선택한 대학 정보 불러오기
selected_univ = next(u for u in universities if u["name"] == selected_name)

# 지도 출력
st.subheader(f"📍 {selected_univ['name']} 위치")
map_df = pd.DataFrame([[selected_univ["lat"], selected_univ["lon"]]], columns=["lat", "lon"])
st.map(map_df, zoom=15)

# 대학 소개
st.subheader("📝 대학 소개")
st.markdown(selected_univ["desc"])

# 오시는 길
st.subheader("🚶‍♀️ 오시는 길")
st.markdown(selected_univ["how_to_get"])
