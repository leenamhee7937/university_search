import streamlit as st

# 전공별 수도권 대학교 정보
major_universities = {
    "인공지능": ["서울대학교", "고려대학교", "연세대학교", "한양대학교", "성균관대학교"],
    "약학": ["서울대학교", "중앙대학교", "이화여자대학교", "성균관대학교", "경희대학교"],
    "간호": ["서울대학교", "연세대학교", "이화여자대학교", "가톨릭대학교", "한양대학교"],
    "의학": ["서울대학교", "연세대학교", "성균관대학교", "한양대학교", "고려대학교"],
    "컴퓨터": ["서울대학교", "고려대학교", "연세대학교", "한양대학교", "서강대학교"],
    "화학공학": ["서울대학교", "고려대학교", "연세대학교", "한양대학교", "중앙대학교"]
}

# 앱 제목
st.title("📚 수도권 전공별 대학교 찾기")

# 전공 선택 드롭다운
selected_major = st.selectbox("전공을 선택하세요:", list(major_universities.keys()))

# 선택된 전공에 따른 대학교 목록 출력
if selected_major:
    st.subheader(f"🏫 {selected_major} 전공 개설 대학")
    universities = major_universities[selected_major]
    for uni in universities:
        st.markdown(f"- {uni}")
