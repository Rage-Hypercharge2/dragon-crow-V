import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="My Introduction",
    page_icon="👋",
    layout="centered"
)

# 제목
st.title("👋 Hello, I'm Eunsoo Han!")

st.write("---")

# 자기소개
st.header("🙋 About Me")
st.write("""
안녕하세요! 저는 **한은수**입니다.

- 🎓 전공: Computer Science
- 💻 관심 분야: Python, AI, Data Analysis
- 🌱 현재 배우는 것: Streamlit, GitHub, Machine Learning
- 🎯 목표: 다양한 프로젝트를 만들며 개발 역량을 키우는 것
""")

# 기술 스택
st.header("🛠 Skills")
st.write("""
- Python
- Git & GitHub
- Streamlit
- Pandas
- NumPy
""")

# 취미
st.header("🎨 Hobbies")
st.write("""
- 📚 독서
- 🎵 음악 감상
- 💻 코딩
- ☕ 마인크래프트
""")

st.write("---")

# 연락처
st.header("📫 Contact")
st.write("""
- 📧 Email: your_email@example.com
- 🐙 GitHub: https://github.com/your_github_id
""")

st.success("Thanks for visiting my introduction page! 😊")
