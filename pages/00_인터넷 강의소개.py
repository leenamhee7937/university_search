import streamlit as st

# 사이트 정보
study_sites = [
    {
        "name": "메가스터디",
        "emoji": "🚀",
        "description": "전국 1등급 강사들이 포진한 대표적인 고등학생/재수생 대상 플랫폼입니다.",
        "url": "https://www.megastudy.net"
    },
    {
        "name": "이투스",
        "emoji": "🧠",
        "description": "다양한 콘텐츠와 체계적인 커리큘럼이 강점인 입시 전문 사이트입니다.",
        "url": "https://www.etoos.com"
    },
    {
        "name": "대성마이맥",
        "emoji": "🔥",
        "description": "임팩트 있는 강의와 강한 학습 동기 부여로 유명한 사이트입니다.",
        "url": "https://www.mimacstudy.com"
    },
    {
        "name": "EBSi",
        "emoji": "📺",
        "description": "무료로 제공되는 공신력 있는 EBS 강의. 수능 연계 대비에 강력 추천!",
        "url": "https://www.ebsi.co.kr"
    },
    {
        "name": "스카이에듀",
        "emoji": "🌈",
        "description": "다양한 강사진과 프리패스로 경제적인 수강이 가능한 플랫폼입니다.",
        "url": "https://www.skyedu.com"
    }
]

# -------------------- Streamlit 구성 --------------------

st.set_page_config(page_title="인터넷 강의 플랫폼 소개", page_icon="📚")

# 별빛 배경 효과
st.markdown("""
<style>
body {
    background: radial-gradient(circle, #f0f8ff, #ffffff);
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
    background: #ffe4e1;
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
    f'<div class="star" style="top: {i*5 % 100}%; left: {i*11 % 100}%; animation-delay: {i*0.2}s;"></div>'
    for i in range(60)
]) + "</div>", unsafe_allow_html=True)

# 타이틀
st.title("✨ 고등학생 & 재수생을 위한 인터넷 강의 사이트 소개")

st.markdown("수험생 여러분, 오늘도 고생 많았어요! 아래는 여러분의 공부를 도와줄 💻 **인터넷 강의 플랫폼**입니다. 믿고 선택해보세요!")

# 사이트 목록 출력
for site in study_sites:
    with st.container():
        st.markdown(f"### {site['emoji']} [{site['name']}]({site['url']})")
        st.markdown(f"{site['description']}")
        st.markdown("---")

# 응원 멘트
st.subheader("🎯 응원 메시지")
st.markdown("""
💬 *공부가 힘들 때도 있지만, 당신의 꿈은 그만큼 가치 있습니다.*  
🌟 *포기하지 마세요. 당신의 노력은 반드시 빛을 발할 거예요.*  
📚 *오늘의 작은 성취가 내일의 큰 변화를 만듭니다!*  
""")

st.success("당신의 수험생활을 진심으로 응원합니다! 🌸 화이팅! 💪")

