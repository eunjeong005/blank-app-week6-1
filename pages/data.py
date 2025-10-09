
import streamlit as st
import pandas as pd
import numpy as np

st.info('matplotlib 기반의 커스텀 그래프를 사용하려면 requirements.txt에 matplotlib를 추가해야 합니다. 예: matplotlib>=3.0.0')

st.title('데이터 분석 예시')

# 샘플 데이터 생성
np.random.seed(42)
df = pd.DataFrame({
	'연도': [2021, 2022, 2023, 2024, 2025],
	'매출액': np.random.randint(100, 500, 5),
	'고객수': np.random.randint(50, 200, 5)
})

st.subheader('샘플 데이터')
st.dataframe(df)

st.subheader('매출액 추이')
st.line_chart(df.set_index('연도')['매출액'])

st.subheader('고객수 추이')
st.bar_chart(df.set_index('연도')['고객수'])

st.subheader('기초 통계')
st.write(df.describe())

st.subheader('상관관계 분석')
st.write(df.corr(numeric_only=True))

# matplotlib 예시
st.subheader('matplotlib로 그린 산점도')
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(df['매출액'], df['고객수'], color='tomato')
ax.set_xlabel('매출액')
ax.set_ylabel('고객수')
ax.set_title('매출액 vs 고객수 산점도')
st.pyplot(fig)

# matplotlib을 반드시 활용해야 하는 예시 (예: pie chart, histogram 등)
st.subheader('matplotlib로 그린 파이차트')
labels = df['연도'].astype(str)
sizes = df['매출액']
fig2, ax2 = plt.subplots()
ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax2.set_title('연도별 매출액 비율')
st.pyplot(fig2)

st.subheader('matplotlib로 그린 히스토그램')
fig3, ax3 = plt.subplots()
ax3.hist(df['고객수'], bins=5, color='skyblue', edgecolor='black')
ax3.set_xlabel('고객수')
ax3.set_ylabel('빈도')
ax3.set_title('고객수 분포 히스토그램')
st.pyplot(fig3)
