import streamlit as st

# 전공별 수도권 대학교 및 진로 정보
major_data = {
    "인공지능": {
        "universities": ["서울대학교", "고려대학교", "연세대학교", "한양대학교", "성균관대학교"],
        "career": [
            "AI 연구원 🤖",
            "데이터 사이언티스트 📊",
            "자율주행 개발자 🚗",
            "AI 스타트업 창업자 💡"
        ]
    },
    "약학": {
        "universities": ["서울대학교", "중앙대학교", "이화여자대학교", "성균관대학교", "경희대학교"],
        "career": [
            "약사 💊",
            "제약회사 연구원 🧪",
            "병원 약제부 근무 🏥",
            "의약품 개발자 🔬"
        ]
    },
    "간호": {
        "universities": ["서울대학교", "연세대학교", "이화여자대학교", "가톨릭대학교", "한양대학교"],
        "career": [
            "임상 간호사 👩‍⚕️",
            "보건교사 🏫",
            "공공의료기관 근무 👨‍⚕️",
            "해외 간호사 ✈️"
        ]
    },
    "의학": {
        "universities": ["서울대학교", "연세대학교", "성균관대학교", "한양대학교", "고려대학교"],
        "career": [
            "의사 👨‍⚕️",
            "의과학 연구자 🔬",
            "의료 컨설턴트 📋",
            "공공보건 전문가 🏥"
        ]
    },
    "컴퓨터": {
        "universities": ["서울대학교", "고려대학교", "연세대학교", "한양대학교", "서강대학교"],
        "career": [
            "소프트웨어 개발자 💻",
            "웹/앱 개발자 📱",
            "보안 전문가 🔐",
            "게임 개발자 🎮"
        ]
    },
    "화학공학": {
        "universities": ["서울대학교", "고려대학교", "연세대학교", "한양대학교", "중앙대학교"],
        "career": [
            "화학 엔지니어 ⚗️",
            "석유화학 기업 연구원 🛢️",
            "배터리/소재 개발자 🔋",
            "환경 기술 전문가 🌿"
        ]
    }
}

# ----------------- UI 구성 -----------------

st.set_page_config(page_title="수도권 대학 찾기", page_icon="🎓")
st.title("🎀 수도권 전공별 대학 탐색기")
st.markdown("전공을 선택하거나 검색하여, 해당 전공이 개설된 대학과 졸업 후 진로를 확인하세요! 💡")

# 전공 필터 입력
search_input = st.text_input("🔍 전공 검색:", "")

# 필터링된 전공 리스트 생성
filtered_majors = [major for major in major_data if search_input.strip() in major]

# 전공 선택
selected_major = st.selectbox("👇 전공을 선택하세요:", filtered_majors if filtered_majors else list(major_data.keys()))

# 결과 표시
if selected_major:
    st.subheader(f"🏫 {selected_major} 전공 개설 대학")
    for uni in major_data[selected_major]["universities"]:
        st.markdown(f"- {uni} 🎓")
    
    st.subheader("🌟 졸업 후 진로 분야")
    for job in major_data[selected_major]["career"]:
        st.markdown(f"- {job}")
    
    st.success(f"'{selected_major}' 전공에 관심 있는 당신을 응원합니다! 🌈")
