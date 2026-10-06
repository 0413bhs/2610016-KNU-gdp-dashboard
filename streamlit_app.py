import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Streamlit 요소 체험실",
    page_icon=":test_tube:",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(ellipse at 8% 0%, rgba(193, 232, 216, .48), transparent 34%),
            linear-gradient(150deg, #f8f8f2 0%, #edf4f1 100%);
        color: #1d332d;
    }
    [data-testid="stHeader"] { background: rgba(248, 248, 242, .72); }
    .block-container { max-width: 1120px; padding-top: 2.6rem; padding-bottom: 4rem; }
    h1, h2, h3 { color: #1d332d; letter-spacing: 0; }
    h1 { font-size: 2.65rem; }
    [data-testid="stCaptionContainer"] { color: #59736a; }
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, .68);
        border: 1px solid rgba(44, 91, 73, .14);
        border-radius: 8px;
        padding: 1rem 1.2rem;
    }
    [data-testid="stTabs"] button { font-weight: 650; }
    div.stButton > button[kind="primary"] {
        background: #176b53;
        border-color: #176b53;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.caption("STREAMLIT FIELD GUIDE  /  인터랙티브 입문")
st.title("화면을 직접 움직이며 배우는 Streamlit")
st.write(
    "Streamlit은 Python 코드 몇 줄로 데이터 앱을 만드는 도구예요. "
    "아래 예제를 바꿔 보면서 입력이 화면에 어떻게 반영되는지 확인해 보세요."
)
st.info("왼쪽부터 탭을 눌러 살펴보세요. 위젯을 조작하면 앱이 다시 실행되며 결과가 갱신됩니다.")

text_tab, input_tab, data_tab = st.tabs(["01  화면과 피드백", "02  입력과 선택", "03  표와 차트"])

with text_tab:
    st.header("텍스트와 상태 메시지")
    st.caption("제목, 설명, 안내 상자로 정보를 읽기 쉽게 나눕니다.")

    text_col, message_col = st.columns([1.2, 1], gap="large")
    with text_col:
        st.subheader("텍스트 요소")
        st.write("`st.write`는 텍스트와 데이터를 간편하게 보여주는 기본 출력 함수입니다.")
        st.markdown("**Markdown**으로 굵은 글씨, 목록, [링크](https://streamlit.io/)도 표현할 수 있어요.")
        st.code('st.title("나의 첫 앱")\nst.write("화면에 내용을 표시해요.")', language="python")
    with message_col:
        st.subheader("상태 알림")
        st.success("success: 작업이 잘 끝났을 때")
        st.warning("warning: 확인이 필요할 때")
        st.error("error: 문제가 생겼을 때")
        st.info("info: 참고할 내용을 안내할 때")

    st.divider()
    st.subheader("버튼과 접을 수 있는 설명")
    left, right = st.columns([1, 2], gap="large")
    with left:
        st.write("버튼을 누르면 앱이 다시 실행되고, 클릭 결과를 확인할 수 있어요.")
        if st.button("인사 받기", type="primary"):
            st.toast("반가워요! 버튼 입력이 전달됐습니다.", icon=":material/waving_hand:")
            st.success("버튼이 눌렸어요. 클릭 결과를 앱에 표시할 수 있습니다.")
    with right:
        with st.expander("여기를 눌러 더 알아보기"):
            st.write("`st.expander`는 자주 보지 않는 세부 설명을 접어 두어 화면을 깔끔하게 유지합니다.")
            st.caption("긴 도움말이나 선택적인 세부 정보에 잘 어울려요.")

with input_tab:
    st.header("입력과 선택")
    st.caption("텍스트, 숫자, 날짜, 선택 위젯의 값을 바꾸고 아래 미리보기에서 확인해 보세요.")

    left_col, right_col = st.columns(2, gap="large")
    with left_col:
        learner_name = st.text_input("이름", value="새싹 학습자", help="한 줄 텍스트를 입력합니다.")
        goal = st.text_area("오늘의 목표", value="Streamlit 위젯을 하나씩 눌러 보기", height=100)
        study_minutes = st.slider("오늘 공부한 시간", min_value=0, max_value=180, value=45, step=15, format="%d분")
        confidence = st.select_slider("현재 익숙함", options=["처음이에요", "조금 알아요", "익숙해요", "잘 알아요"], value="조금 알아요")
        age = st.number_input("학습 일수", min_value=1, max_value=365, value=7, step=1)
    with right_col:
        topic = st.selectbox("먼저 배울 주제", ["텍스트", "입력 위젯", "데이터 표", "차트"])
        interests = st.multiselect(
            "관심 있는 요소 (여러 개 선택)",
            ["버튼", "슬라이더", "체크박스", "차트", "데이터 편집"],
            default=["슬라이더", "차트"],
        )
        pace = st.radio("진행 방식", ["천천히", "기본", "빠르게"], horizontal=True)
        wants_reminder = st.checkbox("학습 알림을 받고 싶어요", value=True)
        include_weekend = st.toggle("주말 학습도 포함", value=False)
        start_date = st.date_input("시작 날짜")

    st.subheader("입력 결과 미리보기")
    preview_col, progress_col = st.columns([1.4, 1], gap="large")
    with preview_col:
        st.write(f"**{learner_name or '이름 없음'}** 님의 오늘 목표는 **{goal or '아직 입력하지 않았어요'}** 입니다.")
        st.write(f"먼저 배울 주제: `{topic}` · 진행 방식: `{pace}` · 익숙함: `{confidence}`")
        st.write(f"관심 요소: {', '.join(interests) if interests else '선택 없음'}")
        st.caption(f"시작일 {start_date} · 학습 계획 {age}일 · 알림 {'켜짐' if wants_reminder else '꺼짐'} · 주말 {'포함' if include_weekend else '미포함'}")
    with progress_col:
        st.metric("오늘의 학습 시간", f"{study_minutes}분", delta=f"목표 60분까지 {max(60 - study_minutes, 0)}분")
        st.progress(min(study_minutes / 60, 1.0), text="60분 목표")

    with st.form("quick_form"):
        st.write("**폼으로 한 번에 제출하기**")
        form_answer = st.text_input("Streamlit에서 만들어 보고 싶은 앱은?", placeholder="예: 나만의 독서 기록장")
        submitted = st.form_submit_button("답변 제출")
    if submitted:
        st.success(f"좋은 아이디어예요! {'“' + form_answer + '”' if form_answer else '답변을 입력하지 않았어요.'}")
    st.caption("폼 안의 위젯은 제출 버튼을 눌렀을 때 한 번에 전달됩니다.")

with data_tab:
    st.header("표, 차트, 숫자 요약")
    st.caption("표를 직접 편집하면 요약 수치와 차트에도 변경 내용이 반영됩니다.")

    study_data = pd.DataFrame(
        {
            "과목": ["Python", "Streamlit", "데이터 분석", "시각화"],
            "공부 시간(분)": [40, 55, 35, 25],
            "완료": [True, True, False, False],
        }
    )
    st.write("**편집 가능한 데이터 표** · 시간과 완료 여부를 바꿔 보세요.")
    edited_data = st.data_editor(
        study_data,
        hide_index=True,
        width="stretch",
        num_rows="fixed",
        column_config={
            "과목": st.column_config.TextColumn("과목", disabled=True),
            "공부 시간(분)": st.column_config.NumberColumn("공부 시간(분)", min_value=0, max_value=300, step=5),
            "완료": st.column_config.CheckboxColumn("완료"),
        },
    )

    completed_count = int(edited_data["완료"].sum())
    total_minutes = int(edited_data["공부 시간(분)"].sum())
    metric_one, metric_two, metric_three = st.columns(3)
    metric_one.metric("등록한 과목", f"{len(edited_data)}개")
    metric_two.metric("총 공부 시간", f"{total_minutes}분")
    metric_three.metric("완료한 과목", f"{completed_count}개", delta=f"전체 {len(edited_data)}개")

    chart_left, chart_right = st.columns(2, gap="large")
    with chart_left:
        st.subheader("막대 차트")
        st.caption("과목별 공부 시간을 비교합니다.")
        st.bar_chart(edited_data, x="과목", y="공부 시간(분)", color="#176b53")
    with chart_right:
        st.subheader("선 차트")
        st.caption("슬라이더에서 선택한 공부 시간의 누적 흐름을 보여줍니다.")
        daily_data = pd.DataFrame({"일차": list(range(1, 8)), "누적 시간(분)": [20, 45, 75, 100, 140, 175, 220]})
        daily_data["누적 시간(분)"] = daily_data["누적 시간(분)"].clip(upper=max(study_minutes * 5, 20))
        st.line_chart(daily_data, x="일차", y="누적 시간(분)", color="#e17d55")

    csv_data = edited_data.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "편집한 표 CSV로 다운로드",
        data=csv_data,
        file_name="streamlit-학습기록.csv",
        mime="text/csv",
    )

st.divider()
st.caption("Streamlit은 위젯 입력이 바뀔 때마다 Python 스크립트를 위에서 아래로 다시 실행합니다.")
