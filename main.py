import streamlit as st

# 전공별 수도권 대학 정보 (홈페이지, 최저학력기준, 진로)
major_data = {
    "인공지능": {
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr"} : "국·수·탐 평균 1.5등급 이내 + 영어 2등급 이내"
            "고려대학교": {"url": "https://www.korea.ac.kr", "cut": "3개 영역 등급 합 5 이내 (국, 수, 탐 중)"},
            "연세대학교": {"url": "https://www.yonsei.ac.kr", "cut": "국·수·영·탐 중 3개 영역 등급 합 6 이내"},
            "한양대학교": {"url": "https://www.hanyang.ac.kr", "cut": "최저학력 기준 없음"},
            "성균관대학교": {"url": "https://www.skku.edu", "cut": "2개 영역 등급 합 4 이내 (국, 수, 영, 탐 중)"},
        },
        "career": ["AI 연구원 🤖", "데이터 사이언티스트 📊", "자율주행 개발자 🚗", "AI 스타트업 창업자 💡"]
    },
    "약학": {
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국수탐 평균 1.5등급 이내 + 영어 2등급 이내"},
            "중앙대학교": {"url": "https://www.cau.ac.kr", "cut": "국·수·영·탐 중 3개 영역 등급 합 6 이내"},
            "이화여자대학교": {"url": "https://www.ewha.ac.kr", "cut": "3개 영역 등급 합 5 이내 (국, 수, 탐 중)"},
            "성균관대학교": {"url": "https://www.skku.edu", "cut": "2개 영역 등급 합 4 이내"},
            "경희대학교": {"url": "https://www.khu.ac.kr", "cut": "국·수·영·탐 중 2개 영역 등급 합 4 이내"},
        },
        "career": ["약사 💊", "제약회사 연구원 🧪", "병원 약제부 근무 🏥", "의약품 개발자 🔬"]
    },
    "간호": {
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국수탐 평균 2등급 이내"},
            "연세대학교": {"url": "https://www.yonsei.ac.kr", "cut": "3개 영역 등급 합 6 이내"},
            "이화여자대학교": {"url": "https://www.ewha.ac.kr", "cut": "3개 영역 등급 합 5 이내"},
            "가톨릭대학교": {"url": "https://www.catholic.ac.kr", "cut": "국·수·영·탐 중 2개 영역 2등급 이내"},
            "한양대학교": {"url": "https://www.hanyang.ac.kr", "cut": "최저학력 기준 없음"},
        },
        "career": ["임상 간호사 👩‍⚕️", "보건교사 🏫", "공공의료기관 근무 👨‍⚕️", "해외 간호사 ✈️"]
    },
    "의학": {
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국수탐 평균 1.5등급 이내"},
            "연세대학교": {"url": "https://www.yonsei.ac.kr", "cut": "국·수·영·탐 중 3개 영역 등급 합 4 이내"},
            "성균관대학교": {"url": "https://www.skku.edu", "cut": "3개 영역 등급 합 5 이내"},
            "한양대학교": {"url": "https://www.hanyang.ac.kr", "cut": "최저학력 기준 없음"},
            "고려대학교": {"url": "https://www.korea.ac.kr", "cut": "3개 영역 등급 합 5 이내"},
        },
        "career": ["의사 👨‍⚕️", "의과학 연구자 🔬", "의료 컨설턴트 📋", "공공보건 전문가 🏥"]
    },
    "컴퓨터": {
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국수탐 평균 1.5등급 이내"},
            "고려대학교": {"url": "https://www.korea.ac.kr", "cut": "3개 영역 등급 합 5 이내"},
            "연세대학교": {"url": "https://www.yonsei.ac.kr", "cut": "3개 영역 등급 합 6 이내"},
            "한양대학교": {"url": "https://www.hanyang.ac.kr", "cut": "최저학력 기준 없음"},
            "서강대학교": {"url": "https://www.sogang.ac.kr", "cut": "2개 영역 등급 합 4 이내"},
        },
        "career": ["소프트웨어 개발자 💻", "웹/앱 개발자 📱", "보안 전문가 🔐", "게임 개발자 🎮"]
    },
    "화학공학": {
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국수탐 평균 1.5등급 이내"},
            "고려대학교": {"url": "https://www.korea.ac.kr", "cut": "3개 영역 등급 합 5 이내"},
            "연세대학교": {"url": "https://www.yonsei.ac.kr", "cut": "3개 영역 등급 합 6 이내"},
            "한양대학교": {"url": "https://www.hanyang.ac.kr", "cut": "최저학력 기준 없음"},
            "중앙대학교": {"url": "https://www.cau.ac.kr", "cut": "2개 영역 등급 합 4 이내"},
        },
        "career": ["화학 엔지니어 ⚗️", "석유화학 연구원 🛢️", "배터리 소재 개발자 🔋", "환경 기술 전문가 🌿"]
    }
}

# -------------------- Streamlit 구성 --------------------

st.set_page_config(page_title="수도권 대학 찾기", page_icon="🎓")

# 별빛 배경 효과
st.markdown("""
<style>
body {
    background: radial-gradient(circle, #fdf6e3, #ffffff);
    overflow: hidden;
}
#stars {
    position: fixed;
    width: 100%;
    height: 100%;
    background: transparent;
    z-index: -1;
}
.star {
    position: absolute;
    width: 2px;
    height: 2px;
    background: #ffccff;
    border-radius: 50%;
    animation: twinkle 2s infinite ease-in-out alternate;
}
@keyframes twinkle {
    from { opacity: 0.2; }
    to { opacity: 1; }
}
</style>
<div id="stars">
""" + "\n".join([
    f'<div class="star" style="top: {i*3 % 100}%; left: {i*7 % 100}%; animation-delay: {i*0.3}s;"></div>'
    for i in range(50)
]) + "</div>", unsafe_allow_html=True)

# 제목
st.title("✨ 수도권 전공별 대학 탐색기")
st.markdown("전공을 선택하면 개설 대학, 홈페이지, 교과전형 최저학력 기준, 졸업 후 진로 정보를 볼 수 있어요! 🎓")

# 전공 검색 및 선택
#search_input = st.text_input("🔍 전공 검색:", "")
#filtered_majors = [major for major in major_data if search_input.strip() in major]
selected_major = st.selectbox("👇 전공을 선택하세요:", filtered_majors if filtered_majors else list(major_data.keys()))

# 결과 출력
if selected_major:
    st.subheader(f"🏫 {selected_major} 전공 개설 대학")

    for uni, info in major_data[selected_major]["universities"].items():
        with st.container():
            st.markdown(f"### [{uni}]({info['url']})")
            st.markdown(f"📚 **교과전형 최저학력기준**: {info['cut']}")
            st.markdown("---")

    st.subheader("🌟 졸업 후 진로 분야")
    for job in major_data[selected_major]["career"]:
        st.markdown(f"- {job}")

    st.success(f"'{selected_major}' 전공에 관심 있는 당신을 응원합니다! 🎉")
