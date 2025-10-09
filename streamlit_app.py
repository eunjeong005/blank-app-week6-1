import streamlit as st

st.title("🎈 Streamlit 요소 데모")
st.header("1. 텍스트 요소")
st.text('이것은 일반 텍스트입니다.')
st.markdown('**마크다운** _스타일링_ 지원')
st.caption('캡션: 부가 설명')
st.code('print("Hello, Streamlit!")', language='python')
st.latex(r'\alpha^2 + \beta^2 = \gamma^2')

st.header("2. 데이터 표시")
st.write({'키': '값', '숫자': 123})
st.json({'name': '홍길동', 'age': 30, 'job': '개발자'})
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=['A', 'B', 'C']
)
st.dataframe(df)
st.table(df.head(3))

st.header("3. 차트와 그래프")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

st.header("4. 입력 위젯")
name = st.text_input('이름을 입력하세요')
age = st.number_input('나이', min_value=0, max_value=120, value=25)
agree = st.checkbox('동의합니다')
selected = st.radio('성별', ['남성', '여성', '기타'])
option = st.selectbox('좋아하는 동물', ['강아지', '고양이', '토끼'])
multi = st.multiselect('좋아하는 색상', ['빨강', '파랑', '초록', '노랑'])
date = st.date_input('날짜 선택')
time = st.time_input('시간 선택')
st.file_uploader('파일 업로드')
st.color_picker('색상 선택')

st.header("5. 버튼과 상호작용")
if st.button('클릭!'):
    st.success('버튼이 눌렸어요!')
st.download_button('텍스트 다운로드', '이것은 다운로드할 텍스트입니다.', file_name='sample.txt')

st.header("6. 슬라이더")
value = st.slider('값을 선택하세요', 0, 100, 50)
st.write('선택한 값:', value)

st.header("7. 진행상황 표시")
st.progress(70)
with st.spinner('로딩 중...'):
    import time
    time.sleep(0.5)
st.success('로딩 완료!')

st.header("8. 사이드바")
st.sidebar.title('사이드바')
st.sidebar.button('사이드바 버튼')
st.sidebar.selectbox('사이드바 선택', ['A', 'B', 'C'])

st.header("9. 미디어")
st.image('https://static.streamlit.io/examples/cat.jpg', caption='고양이')
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')
st.video('https://www.youtube.com/watch?v=5qap5aO4i9A')

st.header("10. 기타")
st.error('에러 메시지')
st.warning('경고 메시지')
st.info('정보 메시지')
st.success('성공 메시지')
st.exception(Exception('예외 메시지'))
