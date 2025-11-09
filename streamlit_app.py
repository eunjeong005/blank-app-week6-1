import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="이차함수 학습")

# --- 세션 상태 초기화 ---
if "moved" not in st.session_state:
    st.session_state.moved = False
if "a" not in st.session_state:
    st.session_state.a = 3
if "b" not in st.session_state:
    st.session_state.b = 12
if "c" not in st.session_state:
    st.session_state.c = -5

# 목표는 초기값과 다르게 설정해서 "아직 성공"이 안 뜨도록 함
if "target" not in st.session_state:
    st.session_state.target = {"a": 3, "b": 30, "c": -5}

# 고유 scope의 CSS: Streamlit 외부 스타일에 의존하지 않도록 앱 내부에서 렌더링
st.markdown(
    """
<style>
#custom-app { padding: 40px 36px; background: linear-gradient(180deg,#6f77ff 0%, #6f77ff 100%); }
#custom-app .top-title { font-size:44px; font-weight:800; color:#1f2937; margin-bottom:18px; display:flex; align-items:center; gap:12px; }
#custom-app .center-card { background:#fff; border-radius:12px; padding:22px; border:1px solid rgba(0,0,0,0.06); box-shadow:0 6px 0 rgba(0,0,0,0.04); width:100%; }
#custom-app .blue-banner { background: linear-gradient(180deg,#e9f2ff,#d7ecff); border:2px solid #2f8bff; border-radius:10px; padding:16px; text-align:center; margin-bottom:18px; }
#custom-app .blue-banner h2 { color:#0b61d6; font-size:22px; margin:0; }
#custom-app .choice-row { display:flex; gap:24px; justify-content:center; margin-top:12px; }
#custom-app .choice { width:170px; height:110px; border-radius:12px; background:#f0f8ff; border:2px solid #2f8bff; display:flex; flex-direction:column; align-items:center; justify-content:center; font-weight:700; color:#0b61d6; }
#custom-app .small-note { font-size:13px; color:#222; margin-top:10px; text-align:center; }
</style>
""",
    unsafe_allow_html=True,
)

# 앱 내부 마크업 (Streamlit 외부 레이아웃에 덮어써지지 않음)
st.markdown('<div id="custom-app">', unsafe_allow_html=True)

st.markdown('<div class="top-title">🎯 <span>이차함수 완전제곱식 & 그래프 변환 학습</span></div>', unsafe_allow_html=True)

st.markdown('<div class="center-card">', unsafe_allow_html=True)

# 오른쪽 상단 초기화(다시하기)
colL, colR = st.columns([9,1])
with colR:
    if st.button("다시하기"):
        st.session_state.a = 3
        st.session_state.b = 12
        st.session_state.c = -5
        st.session_state.moved = False
        st.experimental_rerun()

# 파란 배너
st.markdown('<div class="blue-banner">', unsafe_allow_html=True)
st.markdown(f'<h2>원래 이차식: <em>y = {st.session_state.a}x<sup>2</sup> + {st.session_state.b}x + {st.session_state.c}</em></h2>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 안내문
st.markdown(f'<div class="small-note">🧐 목표: y = {st.session_state.target["a"]}x² + {st.session_state.target["b"]}x + {st.session_state.target["c"]} 과 같은 개형을 가진 그래프를 선택하세요:</div>', unsafe_allow_html=True)

# 선택지 (시각적으로 동일하게 보이도록 내부에서 렌더링)
st.markdown('<div class="choice-row">', unsafe_allow_html=True)
c1, c2 = st.columns([1,1])
with c1:
    if st.button("아래로 볼록 (+x²)"):
        st.session_state.a = abs(st.session_state.a) if st.session_state.a != 0 else 1
        st.session_state.moved = True
        st.experimental_rerun()
    st.markdown('<div class="choice"><div style="font-size:40px;margin-bottom:6px">U</div>아래로 볼록 (+x²)</div>', unsafe_allow_html=True)
with c2:
    if st.button("위로 볼록 (-x²)"):
        st.session_state.a = -abs(st.session_state.a) if st.session_state.a != 0 else -1
        st.session_state.moved = True
        st.experimental_rerun()
    st.markdown('<div class="choice"><div style="font-size:40px;margin-bottom:6px">∩</div>위로 볼록 (-x²)</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)
st.write("현재 계수:", f"a = {st.session_state.a}, b = {st.session_state.b}, c = {st.session_state.c}")

# 그래프를 크게 그려서 4/5 사진처럼 보이게 함
x = np.linspace(-10, 10, 600)
y = st.session_state.a * x**2 + st.session_state.b * x + st.session_state.c
fig, ax = plt.subplots(figsize=(7, 4.8), dpi=100)
ax.plot(x, y, color="#0b62ff", linewidth=2)
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.set_xlim(-8, 8)
ymin, ymax = y.min(), y.max()
yrange = max(1.0, ymax - ymin)
ax.set_ylim(ymin - 0.25 * yrange, ymax + 0.25 * yrange)
ax.grid(which="both", linestyle=":", linewidth=0.6, alpha=0.7)
st.pyplot(fig, clear_figure=True)

st.markdown('</div>', unsafe_allow_html=True)  # center-card
st.markdown('</div>', unsafe_allow_html=True)  # custom-app

# 성공 메시지: 반드시 사용자가 버튼 클릭으로 moved=True 된 경우에만 표시
current = (st.session_state.a, st.session_state.b, st.session_state.c)
target = (st.session_state.target["a"], st.session_state.target["b"], st.session_state.target["c"])
if st.session_state.moved and current == target:
    st.success("🎉 완벽합니다! 한 번에 성공하셨네요!")
