import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os

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

if "target" not in st.session_state:
    st.session_state.target = {"a": 3, "b": 12, "c": -5}

# 강제 스타일: 전체 배경 + 중앙 카드 + 파란 배너 등
st.markdown(
    """
<style>
/* 페이지 배경 그라데이션 */
.block-container { padding-top: 8rem; padding-left:4rem; padding-right:4rem; }
section.main { background: linear-gradient(180deg,#6f77ff 0%, #6f77ff 100%); padding: 3rem 0; }

/* 큰 헤더 (상단 로고/타이틀) */
.app-title {
  font-size: 48px;
  font-weight: 800;
  color: #1f2937;
  display:flex;
  align-items:center;
  gap:12px;
  margin-bottom: 1rem;
}

/* 중앙 카드 */
.center-card {
  width: 92%;
  margin: 0 auto;
  background: #ffffff;
  border-radius: 12px;
  padding: 26px 28px;
  box-shadow: 0 6px 0 rgba(0,0,0,0.04);
  border: 1px solid rgba(0,0,0,0.06);
}

/* 파란 배너 (큰 타이틀 박스) */
.blue-banner {
  background: linear-gradient(180deg,#e9f2ff,#d7ecff);
  border: 2px solid #2f8bff;
  border-radius:10px;
  padding: 18px;
  text-align:center;
  margin-bottom: 26px;
}
.blue-banner h2 { color:#0b61d6; font-size:26px; margin:0; }

/* 버튼 모양 (선택지) */
.choice-row { display:flex; gap:28px; justify-content:center; margin-top:6px; }
.choice {
  width:170px;
  height:120px;
  border-radius:12px;
  background:#f0f8ff;
  border:2px solid #2f8bff;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  font-weight:600;
  color:#0b61d6;
  cursor:pointer;
}
.choice .icon { font-size:42px; margin-bottom:8px; }
.small-note { font-size:13px; color:#222; margin-top:14px; text-align:center; }

/* 오른쪽 reset 버튼 위치 보정 (기존 레이아웃과 유사하게) */
.reset-btn { float:right; margin-top:-6px; }
</style>
""",
    unsafe_allow_html=True,
)

# 상단 큰 제목
st.markdown(f'<div class="app-title">🎯 <span>이차함수 완전제곱식 & 그래프 변환 학습</span></div>', unsafe_allow_html=True)

# 중앙 카드 시작
st.markdown('<div class="center-card">', unsafe_allow_html=True)

# 오른쪽 상단 다시하기(초기화) 버튼 위치(간단)
reset_col1, reset_col2 = st.columns([9,1])
with reset_col2:
    if st.button("다시하기"):
        st.session_state.a = 3
        st.session_state.b = 12
        st.session_state.c = -5
        st.session_state.moved = False
        st.experimental_rerun()

# 파란 배너(타이틀 영역)
st.markdown('<div class="blue-banner">', unsafe_allow_html=True)
st.markdown(f'<h2>원래 이차식:  <em>y = {st.session_state.a}x<sup>2</sup> + {st.session_state.b}x + {st.session_state.c}</em></h2>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 안내 텍스트(한줄)
st.markdown(f'<div class="small-note">🧐 목표: y = {st.session_state.target["a"]}x² + {st.session_state.target["b"]}x + {st.session_state.target["c"]} 과 같은 개형을 가진 그래프를 선택하세요:</div>', unsafe_allow_html=True)

# 선택지 버튼들(시각적) — 실제 동작은 st.button으로 처리
st.markdown('<div class="choice-row">', unsafe_allow_html=True)

col_a, col_b = st.columns([1,1])
with col_a:
    if st.button("아래로 볼록 (+x²)"):
        # 예시 동작: a positive (정방향 포물선) 선택 시 a>0 유지
        st.session_state.a = abs(st.session_state.a) if st.session_state.a == 0 else abs(st.session_state.a)
        st.session_state.moved = True
        st.experimental_rerun()
    st.markdown('<div class="choice"><div class="icon">U</div>아래로 볼록 (+x²)</div>', unsafe_allow_html=True)
with col_b:
    if st.button("위로 볼록 (-x²)"):
        st.session_state.a = -abs(st.session_state.a) if st.session_state.a == 0 else -abs(st.session_state.a)
        st.session_state.moved = True
        st.experimental_rerun()
    st.markdown('<div class="choice"><div class="icon">∩</div>위로 볼록 (-x²)</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # choice-row end

# 아래에 그래프 / 상태 표시 (작게)
st.markdown('<hr>', unsafe_allow_html=True)
st.write("현재 계수:", f"a = {st.session_state.a}, b = {st.session_state.b}, c = {st.session_state.c}")

# 그래프를 크게 보여주기 (사진 4/5처럼 보였던 동적 그래프)
x = np.linspace(-10, 10, 600)
y = st.session_state.a * x ** 2 + st.session_state.b * x + st.session_state.c
fig, ax = plt.subplots(figsize=(6.4, 4.6), dpi=100)
ax.plot(x, y, color="#0b62ff", linewidth=2)
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.set_xlim(-8, 8)
ymin, ymax = y.min(), y.max()
yrange = max(1.0, ymax - ymin)
ax.set_ylim(ymin - 0.25 * yrange, ymax + 0.25 * yrange)
ax.grid(which="both", linestyle=":", linewidth=0.6, alpha=0.7)
st.pyplot(fig, clear_figure=True)

# 카드 끝
st.markdown('</div>', unsafe_allow_html=True)

# 성공 체크: 사용자 상호작용(버튼 클릭) 후에만 성공 메시지 표시
current = (st.session_state.a, st.session_state.b, st.session_state.c)
target = (st.session_state.target["a"], st.session_state.target["b"], st.session_state.target["c"])
if st.session_state.moved and current == target:
    st.success("🎉 완벽합니다! 한 번에 성공하셨네요!")
