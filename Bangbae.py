import streamlit as st

st.set_page_config(
    page_title="방배중학교 소개",
    page_icon="🏫",
    layout="wide"
)

st.title("🏫 방배중학교 소개")
st.markdown("---")

menu = st.sidebar.radio(
    "메뉴",
    ["학교 소개", "학교 정보", "학교 생활", "오시는 길"]
)

if menu == "학교 소개":

    st.header("환영합니다!")

    st.image(
        "https://images.unsplash.com/photo-1509062522246-3755977927d7?w=1200",
        use_container_width=True
    )

    st.write("""
방배중학교는 서울특별시 서초구에 위치한 공립 중학교입니다.
학생들이 바른 인성과 창의적인 사고를 기를 수 있도록 다양한 교육활동을 운영하고 있습니다.

학교는 학생 중심의 교육을 지향하며,
배움과 성장을 함께하는 행복한 학교를 목표로 하고 있습니다.
""")

    st.success("미래를 준비하는 행복한 학교, 방배중학교")

elif menu == "학교 정보":

    st.header("학교 기본 정보")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("설립", "1980년")
        st.metric("학교 유형", "공립 중학교")

    with col2:
        st.metric("위치", "서울특별시 서초구")
        st.metric("남녀공학", "예")

    st.subheader("학교 특징")

    st.markdown("""
- 📚 다양한 교과 및 창의적 체험활동
- 🎵 문화·예술 교육 활성화
- ⚽ 체육활동 및 스포츠 프로그램
- 💻 디지털 교육과 미래역량 강화
""")

elif menu == "학교 생활":

    st.header("학교 생활")

    tab1, tab2, tab3 = st.tabs(["교육", "동아리", "학교 시설"])

    with tab1:
        st.write("""
학생들의 창의성과 문제 해결 능력을 키우기 위한 다양한 교육 프로그램이 운영됩니다.

- 자유학기 활동
- 진로 탐색
- 프로젝트 수업
- 독서 활동
""")

    with tab2:
        st.write("""
다양한 동아리 활동을 통해 학생들은 자신의 적성과 재능을 발견할 수 있습니다.

- 방송부
- 과학동아리
- 스포츠 동아리
- 음악 동아리
- 미술 동아리
""")

    with tab3:
        st.write("""
학교에는 학생들의 학습과 활동을 위한 다양한 시설이 마련되어 있습니다.

- 도서관
- 과학실
- 컴퓨터실
- 체육관
- 운동장
""")

elif menu == "오시는 길":

    st.header("📍 위치")

    st.write("""
**주소**

서울특별시 서초구 동광로 144
""")

    st.map(
        data={
            "lat":[37.492],
            "lon":[126.988]
        }
    )

    st.info("※ 지도는 학교 위치 주변을 표시한 예시입니다.")

st.markdown("---")

st.caption("© 2026 Bangbae Middle School Introduction Website")streamlit
pandas
