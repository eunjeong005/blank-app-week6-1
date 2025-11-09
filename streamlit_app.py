import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🎯 이차함수 완전제곱식 & 그래프 변환 학습")

# --- 세션 상태 초기화 ---
if "moved" not in st.session_state:
    st.session_state.moved = False
if "a" not in st.session_state:
    st.session_state.a = 5
if "b" not in st.session_state:
    st.session_state.b = 0
if "c" not in st.session_state:
    st.session_state.c = 0

# 목표 계수 (예시)
if "target" not in st.session_state:
    st.session_state.target = {"a": 5, "b": 30, "c": 0}

# CSS: 중앙 정렬 및 박스 스타일 고정 (이미지/그래프의 크기 문제 방지)
st.markdown(
    """
<style>
/* 컨테이너 박스 스타일 */
.container-box {
  border-radius: 10px;
  padding: 18px;
  background: #ffffff;
  box-shadow: none;
}
/* 그래프 캔버스 주변 여백 제거 및 중앙 정렬 */
.streamlit-plot {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
""",
    unsafe_allow_html=True,
)

# 상단 안내 (라텍스 사용)
st.subheader("그래프 평행이동하기")
a0, b0, c0 = st.session_state.a, st.session_state.b, st.session_state.c
st.latex(f"y = {a0}x^2 + {b0}x + {c0}")
t = st.session_state.target
st.write("목표식:", f"y = {t['a']}x^2 + {t['b']}x + {t['c']}")

# 레이아웃: 그래프(왼쪽, 넓게) / 컨트롤(오른쪽)
left, right = st.columns([2.2, 1])

with left:
    st.markdown('<div class="container-box">', unsafe_allow_html=True)
    # 동적으로 그래프를 그려서 항상 같은 비율/크기로 표시 -> 4/5 사진처럼 큼직하게 보임
    x = np.linspace(-10, 10, 600)
    y = st.session_state.a * x ** 2 + st.session_state.b * x + st.session_state.c

    fig, ax = plt.subplots(figsize=(6.0, 5.0), dpi=100)
    ax.plot(x, y, color="#0b62ff", linewidth=2)
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_xlim(-8, 8)
    # y축 범위 자동 + 약간 여유
    ymin, ymax = y.min(), y.max()
    yrange = max(1.0, ymax - ymin)
    ax.set_ylim(ymin - 0.25 * yrange, ymax + 0.25 * yrange)
    ax.grid(which="both", linestyle=":", linewidth=0.6, alpha=0.7)

    # 꼭짓점(vertex) 표시 (눈에 띄게)
    xv = -st.session_state.b / (2 * st.session_state.a) if st.session_state.a != 0 else 0
    yv = st.session_state.a * xv ** 2 + st.session_state.b * xv + st.session_state.c
    ax.plot(xv, yv, "o", color="red")
    ax.annotate(f"({xv:.1f}, {yv:.1f})", xy=(xv, yv), xytext=(xv + 0.8, yv + 0.8),
                arrowprops=dict(arrowstyle="->", color="red"), color="red", fontsize=9)

    st.pyplot(fig, clear_figure=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="container-box">', unsafe_allow_html=True)
    st.write("그래프 이동하기")
    amount = st.number_input("이동량 입력 (정수)", step=1, value=10)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("↑ 위로"):
            st.session_state.c += amount
            st.session_state.moved = True
            st.experimental_rerun()
        if st.button("← 왼쪽"):
            st.session_state.b -= amount
            st.session_state.moved = True
            st.experimental_rerun()
    with col2:
        if st.button("↓ 아래로"):
            st.session_state.c -= amount
            st.session_state.moved = True
            st.experimental_rerun()
        if st.button("→ 오른쪽"):
            st.session_state.b += amount
            st.session_state.moved = True
            st.experimental_rerun()

    if st.button("초기화"):
        st.session_state.a = 5
        st.session_state.b = 0
        st.session_state.c = 0
        st.session_state.moved = False
        st.experimental_rerun()

    st.markdown("---")
    st.write("현재 계수:")
    st.write(f"a = {st.session_state.a},  b = {st.session_state.b},  c = {st.session_state.c}")
    st.markdown('</div>', unsafe_allow_html=True)

# 성공 체크: 반드시 사용자가 이동한 이후에만 성공 메시지 표시
current = (st.session_state.a, st.session_state.b, st.session_state.c)
target = (st.session_state.target["a"], st.session_state.target["b"], st.session_state.target["c"])
if st.session_state.moved and current == target:
    st.success("🎉 완벽합니다! 한 번에 성공하셨네요!")
