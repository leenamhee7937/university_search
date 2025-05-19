import streamlit as st

# 전공별 수도권 대학교, 홈페이지, 진로 정보ㅇ
major_data = {
    "인공지능": {
        "universities": {
            "서울대학교": "https://www.snu.ac.kr",
            "고려대학교": "https://www.korea.ac.kr",
            "연세대학교": "https://www.yonsei.ac.kr",
            "한양대학교": "https://www.hanyang.ac.kr",
            "성균관대학교": "https://www.skku.edu"
        },
        "career": [
            "AI 연구원 🤖",
            "데이터 사이언티스트 📊",
            "자율주행 개발자 🚗",
            "AI 스타트업 창업자 💡"
        ]
    },
    "약학": {
        "universities": {
            "서울대학교": "https://www.snu.ac.kr",
            "중앙대학교": "https://www.cau.ac.kr",
            "이화여자대학교": "https://www.ewha.ac.kr",
            "성균관대학교": "https://www.skku.edu",
            "경희대학교": "https://www.khu.ac.kr"
        },
        "career": [
            "약사 💊",
            "제약회사 연구원 🧪",
            "병원 약제부 근무 🏥",
            "의약품 개발자 🔬"
        ]
    },
    "간호": {
        "universities": {
            "서울대학교": "https://www.snu.ac.kr",
            "연세대학교": "https://www.yonsei.ac.kr",
            "이화여자대학교": "https://www.ewha.ac.kr",
            "가톨릭대학교": "https://www.catholic.ac.kr",
            "한양대학교": "https://www.hanyang.ac.kr"
        },
        "career": [
            "임상 간호사 👩‍⚕️",
            "보건교사 🏫",
            "공공의료기관 근무 👨‍⚕️",
            "해외 간호사 ✈️"
        ]
    },
    "의학": {
        "universities": {
            "서울대학교": "https://www.snu.ac.kr",
            "연세대학교": "https://www.yonsei.ac.kr",
            "성균관대학교": "https://www.skku.edu",
            "한양대학교": "https://www.hanyang.ac.kr",
            "고려대학교": "https://www.korea.ac.kr"
        },
        "career": [
            "의사 👨‍⚕️",
            "의과학 연구자 🔬",
            "의료 컨설턴트 📋",
            "공공보건 전문가 🏥"
        ]
    },
    "컴퓨터": {
        "universities": {
            "서울대학교": "https://www.snu.ac.kr",
            "고려대학교": "https://www.korea.ac.kr",
            "연세대학교": "https://www.yonsei.ac.kr",
            "한양대학교": "https://www.hanyang.ac.kr",
            "서강대학교": "https://www.sogang.ac.kr"
        },
        "career": [
            "소프트웨어 개발자 💻",
            "웹/앱 개발자 📱",
            "보안 전문가 🔐",
            "게임 개발자 🎮"
        ]
    },
    "화학공학": {
        "universities": {
            "서울대학교": "https://www.snu.ac.kr",
            "고려대학교": "https://www.korea.ac.kr",
            "연세대학교": "https://www.yonsei.ac.kr",
            "한양대학교": "https://www.hanyang.ac.kr",
            "중앙대학교": "https://www.cau.ac.kr"
        },
        "career": [
            "화학 엔지니어 ⚗️",
            "석유화학 기업 연구원 🛢️",
            "배터리/소재 개발자 🔋",
            "환경 기술 전문가 🌿"
        ]
    }
}

# ----------------- 스트림릿 구성 -----------------

st.set_page_config(page_title="수도권 대학 찾기", page_icon="🎓")

# 별빛 배경 CSS + JS
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

# UI 타이틀
st.title("✨ 수도권 전공별 대학 탐색기")
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
    for uni, link in major_data[selected_major]["universities"].items():
        st.markdown(f"- [{uni}]({link}) 🌐")

    st.subheader("🌟 졸업 후 진로 분야")
    for job in major_data[selected_major]["career"]:
        st.markdown(f"- {job}")

    st.success(f"'{selected_major}' 전공에 관심 있는 당신을 응원합니다! 🎉")
