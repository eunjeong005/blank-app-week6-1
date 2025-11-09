import streamlit as st

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

# 예시 목표 (화면에 표시될 목표식 — 필요시 동적으로 설정)
if "target" not in st.session_state:
    st.session_state.target = {"a": 5, "b": 30, "c": 0}

# 간단한 이미지 스타일 (이미지 사이즈 고정해서 축소/확대 문제 방지)
st.markdown("""
<style>
img.centered {
  display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 640px;
  height: auto;
}
.container-box {
  border-radius: 10px;
  padding: 20px;
  background: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# 상단 안내
st.subheader("그래프 평행이동하기")
st.write(f"원래 이차함수식: y = {st.session_state.a}x² + {st.session_state.b}x + {st.session_state.c}")
st.write("목표식:", f"y = {st.session_state.target['a']}x² + {st.session_state.target['b']}x + {st.session_state.target['c']}")

# 레이아웃: 이미지(왼쪽) / 컨트롤(오른쪽)
left, right = st.columns([2, 1])
with left:
    st.markdown('<div class="container-box">', unsafe_allow_html=True)
    # 실제 프로젝트에서는 그래프를 동적으로 생성해서 파일로 저장한 뒤 경로를 넣으세요.
    # 여기서는 프로젝트에 있는 정적 이미지가 있다면 그걸 사용합니다.
    # assets/graph_current.png 파일이 없으면 외부 임시 이미지로 대체됩니다.
    import os
    img_path = "assets/graph_current.png"
    if not os.path.exists(img_path):
        img_src = "https://placehold.co/640x480?text=Graph+Placeholder"
        st.markdown(f'<img class="centered" src="{img_src}">', unsafe_allow_html=True)
    else:
        st.image(img_path, use_column_width=False, width=640)
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
        if st.button("← 왼쪽"):
            st.session_state.b -= amount
            st.session_state.moved = True
    with col2:
        if st.button("↓ 아래로"):
            st.session_state.c -= amount
            st.session_state.moved = True
        if st.button("→ 오른쪽"):
            st.session_state.b += amount
            st.session_state.moved = True

    if st.button("초기화"):
        st.session_state.a = 5
        st.session_state.b = 0
        st.session_state.c = 0
        st.session_state.moved = False
        st.experimental_rerun()

    st.markdown("---")
    st.write("현재 계수:", f"a={st.session_state.a}, b={st.session_state.b}, c={st.session_state.c}")
    st.markdown('</div>', unsafe_allow_html=True)

# 성공 체크: 반드시 사용자가 이동한 이후에만 성공 메시지 표시
current = (st.session_state.a, st.session_state.b, st.session_state.c)
target = (st.session_state.target["a"], st.session_state.target["b"], st.session_state.target["c"])
if st.session_state.moved and current == target:
    st.success("🎉 완벽합니다! 한 번에 성공하셨네요!")
else:
    # 성공 메시지를 미리 보여주는 기존 오류를 방지하기 위해 아무 것도 출력하지 않습니다.
    pass
