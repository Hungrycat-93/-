
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ver.17 루틴 뷰어", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_excel("25년운동.xlsx", sheet_name="Ver.17", skiprows=9)
    df.columns = df.columns.astype(str)  # 열 이름 문자열화
    return df

st.title("🏋️‍♂️ Ver.17 루틴 뷰어")

df = load_data()

# 날짜 추출
date_row = df.iloc[0]
routine_date = pd.to_datetime(date_row[0]).strftime("%Y-%m-%d")

st.subheader(f"🗓️ 루틴 날짜: {routine_date}")

# 루틴 시작 부분만 필터링 (운동 종목별 루틴은 보통 4행 이후부터라고 가정)
routine_table = df.iloc[4:10].copy()
routine_table = routine_table.reset_index(drop=True)

st.markdown("### 📋 루틴 구성")
st.dataframe(routine_table)

st.info("※ 현재는 6줄짜리 샘플 루틴만 보여줍니다. 전체 주차별 루틴 기능은 추후 확장 가능합니다.")
