import streamlit as st

# -------------------- 전공별 데이터 --------------------
major_data = {
    "인공지능": {
        "theme_color": "#e6f2ff",
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국·수·탐 평균 1.5등급 이내 + 영어 2등급 이내"},
            "고려대학교": {"url": "https://www.korea.ac.kr", "cut": "3개 영역 등급 합 5 이내"},
            "연세대학교": {"url": "https://www.yonsei.ac.kr", "cut": "국·수·영·탐 중 3개 영역 등급 합 6 이내"},
            "한양대학교": {"url": "https://www.hanyang.ac.kr", "cut": "최저학력 기준 없음"},
            "성균관대학교": {"url": "https://www.skku.edu", "cut": "2개 영역 등급 합 4 이내"},
        },
        "career": ["AI 연구원 🤖", "데이터 사이언티스트 📊", "자율주행 개발자 🚗", "AI 스타트업 창업자 💡"],
        "message": "인공지능 분야는 빠르게 발전하는 미래 산업의 핵심입니다. 논리적 사고력과 창의적 문제 해결 능력을 함께 키워보세요. 수학, 통계, 컴퓨터 지식을 바탕으로 다양한 프로젝트에 도전하면 큰 성장을 이룰 수 있습니다. 당신의 호기심이 큰 가능성을 만듭니다!"
    },
    "약학": {
        "theme_color": "#fff0f5",
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국수탐 평균 1.5등급 이내 + 영어 2등급 이내"},
            "중앙대학교": {"url": "https://www.cau.ac.kr", "cut": "국·수·영·탐 중 3개 영역 등급 합 6 이내"},
            "이화여자대학교": {"url": "https://www.ewha.ac.kr", "cut": "3개 영역 등급 합 5 이내"},
            "성균관대학교": {"url": "https://www.skku.edu", "cut": "2개 영역 등급 합 4 이내"},
            "경희대학교": {"url": "https://www.khu.ac.kr", "cut": "국·수·영·탐 중 2개 영역 등급 합 4 이내"},
        },
        "career": ["약사 💊", "제약회사 연구원 🧪", "병원 약제부 근무 🏥", "의약품 개발자 🔬"],
        "message": "약학은 사람의 건강과 생명을 책임지는 소중한 분야입니다. 꼼꼼함과 책임감, 생명과학에 대한 깊은 이해가 중요합니다. 약사뿐 아니라 제약 연구, 의약개발 등 다양한 진로가 열려 있으니, 폭넓은 관심과 열정으로 준비해보세요!"
    },
    "간호": {
        "theme_color": "#e0f7fa",
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국수탐 평균 2등급 이내"},
            "연세대학교": {"url": "https://www.yonsei.ac.kr", "cut": "3개 영역 등급 합 6 이내"},
            "이화여자대학교": {"url": "https://www.ewha.ac.kr", "cut": "3개 영역 등급 합 5 이내"},
            "가톨릭대학교": {"url": "https://www.catholic.ac.kr", "cut": "2개 영역 2등급 이내"},
            "한양대학교": {"url": "https://www.hanyang.ac.kr", "cut": "최저학력 기준 없음"},
        },
        "career": ["임상 간호사 👩‍⚕️", "보건교사 🏫", "공공의료기관 근무 👨‍⚕️", "해외 간호사 ✈️"],
        "message": "간호학은 생명에 대한 책임감을 바탕으로 실천적 돌봄을 실현하는 전공입니다. 공감 능력과 강한 의지, 체력도 중요한 자산이 됩니다. 국내외 다양한 진로가 열려 있으니, 사람을 향한 따뜻한 마음을 지식과 함께 키워보세요."
    },
    "의학": {
        "theme_color": "#fce4ec",
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국수탐 평균 1.5등급 이내"},
            "연세대학교": {"url": "https://www.yonsei.ac.kr", "cut": "3개 영역 등급 합 4 이내"},
            "성균관대학교": {"url": "https://www.skku.edu", "cut": "3개 영역 등급 합 5 이내"},
            "한양대학교": {"url": "https://www.hanyang.ac.kr", "cut": "최저학력 기준 없음"},
            "고려대학교": {"url": "https://www.korea.ac.kr", "cut": "3개 영역 등급 합 5 이내"},
        },
        "career": ["의사 👨‍⚕️", "의과학 연구자 🔬", "의료 컨설턴트 📋", "공공보건 전문가 🏥"],
        "message": "의학은 사람의 생명을 다루는 전문성과 사명감을 요구하는 길입니다. 긴 학업 과정 속에서도 배움에 대한 열정과 꾸준한 노력이 중요합니다. 다양한 의학 지식과 인성을 갖춘 의사가 되어, 세상에 꼭 필요한 존재가 되어보세요!"
    },
    "컴퓨터": {
        "theme_color": "#e8f5e9",
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국수탐 평균 1.5등급 이내"},
            "고려대학교": {"url": "https://www.korea.ac.kr", "cut": "3개 영역 등급 합 5 이내"},
            "연세대학교": {"url": "https://www.yonsei.ac.kr", "cut": "3개 영역 등급 합 6 이내"},
            "한양대학교": {"url": "https://www.hanyang.ac.kr", "cut": "최저학력 기준 없음"},
            "서강대학교": {"url": "https://www.sogang.ac.kr", "cut": "2개 영역 등급 합 4 이내"},
        },
        "career": ["소프트웨어 개발자 💻", "웹/앱 개발자 📱", "보안 전문가 🔐", "게임 개발자 🎮"],
        "message": "컴퓨터공학은 상상한 것을 현실로 바꾸는 힘을 가진 전공입니다. 논리적 사고, 꾸준한 실습, 협업 능력을 함께 키우세요. 개발 언어, 알고리즘, 시스템을 다루며 IT 세계를 이끄는 주역이 될 수 있습니다!"
    },
    "화학공학": {
        "theme_color": "#fff8e1",
        "universities": {
            "서울대학교": {"url": "https://www.snu.ac.kr", "cut": "국수탐 평균 1.5등급 이내"},
            "고려대학교": {"url": "https://www.korea.ac.kr", "cut": "3개 영역 등급 합 5 이내"},
            "연세대학교": {"url": "https://www.yonsei.ac.kr", "cut": "3개 영역 등급 합 6 이내"},
            "한양대학교": {"url": "https://www.hanyang.ac.kr", "cut": "최저학력 기준 없음"},
            "중앙대학교": {"url": "https://www.cau.ac.kr", "cut": "2개 영역 등급 합 4 이내"},
        },
        "career": ["화학 엔지니어 ⚗️", "석유화학 연구원 🚓", "배터리 소재 개발자 🔋", "환경 기술 전문가 🌿"],
        "message": "화학공학은 실생활과 산업을 연결하는 응용과학입니다. 화학, 수학, 물리에 대한 기초와 함께 실험과 공정 설계에 흥미를 가진다면 큰 발전이 가능합니다. 깨끗한 환경과 에너지 문제 해결에도 기여할 수 있어요!"
    }
}

# -------------------- Streamlit UI --------------------
st.set_page_config(page_title="전공별 수도권 대학 탐색기", page_icon="🎓")

st.title("🎓 전공별 수도권 대학 탐색기🎓 ")
st.markdown("전공을 선택하면 개설 대학, 홈페이지, 교과전형 기준, 진로 및 상담 멘트를 볼 수 있어요! 🎓")
st.markdown("""
<div style='text-align: center;'>
    <img src='https://plus.unsplash.com/premium_vector-1720579367266-571fa03d11e5?q=80&w=2148&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' width='200' height='200'>
    
    
</div>
""", unsafe_allow_html=True)
# 전공 선택
selected_major = st.selectbox("✨ 전공을 선택하세요:", list(major_data.keys()))
selected_theme = major_data[selected_major]["theme_color"]

# 배경색 스타일 적용
st.markdown(f"""
    <style>
    .reportview-container .main .block-container {{
        background-color: {selected_theme};
        padding: 2rem;
        border-radius: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# 출력 내용
st.subheader(f"🏫 {selected_major} 전공 개설 대학")
for uni, info in major_data[selected_major]["universities"].items():
    with st.container():
        st.markdown(f"### [{uni}]({info['url']})")
        st.markdown(f"📚 **교과전형 최저학력기준**: {info['cut']}")
        st.markdown("---")

st.subheader("🌟 졸업 후 진로 분야")
for job in major_data[selected_major]["career"]:
    st.markdown(f"- {job}")

st.subheader("💡 진로 상담 ")
st.markdown(f"🗨️ *{major_data[selected_major]['message']}*")

st.success(f"'{selected_major}' 전공에 도전하는 당신을 응원합니다! 💖")
