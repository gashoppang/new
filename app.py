import streamlit as st
from textwrap import dedent

st.set_page_config(
    page_title="첫 Streamlit 웹앱",
    page_icon="🎉",
    layout="centered",
)

if "page" not in st.session_state:
    st.session_state.page = "main"


def go_greeting():
    st.session_state.page = "greeting"


def go_main():
    st.session_state.page = "main"


st.markdown(
    dedent(
        """
        <style>
        :root {
            --bg: oklch(0.97 0.025 255);
            --bg-soft: oklch(0.93 0.035 255);
            --card: oklch(0.99 0.01 255);
            --text: oklch(0.25 0.03 255);
            --muted: oklch(0.55 0.035 255);
            --accent: oklch(0.68 0.18 255);
            --accent-hover: oklch(0.62 0.2 255);
            --accent-light: oklch(0.88 0.08 255);
            --border: oklch(0.88 0.025 255);
            --shadow: oklch(0.35 0.04 255 / 0.16);
            --white: oklch(1 0 0);
        }

        .stApp {
            background:
                radial-gradient(circle at top, var(--accent-light), transparent 38%),
                linear-gradient(180deg, var(--bg), var(--bg-soft));
            color: var(--text);
        }

        .block-container {
            max-width: 720px;
            padding-top: 12vh;
        }

        .app-card {
            text-align: center;
            padding: 56px 36px;
            border: 1px solid var(--border);
            border-radius: 28px;
            background: var(--card);
            box-shadow: 0 20px 60px var(--shadow);
            overflow: hidden;
        }

        .emoji {
            font-size: 72px;
            line-height: 1;
            margin-bottom: 18px;
        }

        .title {
            margin: 0;
            font-size: 42px;
            font-weight: 800;
            color: var(--text);
            letter-spacing: -0.04em;
        }

        .subtitle {
            margin-top: 14px;
            margin-bottom: 0;
            font-size: 18px;
            color: var(--muted);
        }

        div.stButton {
            display: flex;
            justify-content: center;
            margin-top: 24px;
        }

        div.stButton > button {
            width: 240px;
            height: 52px;
            border-radius: 999px;
            border: 1px solid var(--accent);
            background: var(--accent);
            color: var(--white);
            font-size: 17px;
            font-weight: 700;
            box-shadow: 0 14px 28px oklch(0.45 0.14 255 / 0.28);
            transition: 0.18s ease;
        }

        div.stButton > button:hover {
            border: 1px solid var(--accent-hover);
            background: var(--accent-hover);
            color: var(--white);
            transform: translateY(-2px);
        }

        .fireworks {
            position: relative;
            height: 180px;
            margin-bottom: 12px;
        }

        .spark {
            position: absolute;
            left: var(--left);
            top: var(--top);
            width: 10px;
            height: 10px;
            border-radius: 999px;
            background: var(--color);
            box-shadow: 0 0 18px var(--color);
            animation: boom 1.45s ease-out infinite;
            animation-delay: var(--delay);
            opacity: 0;
        }

        @keyframes boom {
            0% {
                opacity: 0;
                transform: translate(0, 32px) scale(0.2);
            }
            18% {
                opacity: 1;
            }
            100% {
                opacity: 0;
                transform: translate(var(--x), var(--y)) scale(0.85);
            }
        }
        </style>
        """
    ),
    unsafe_allow_html=True,
)


if st.session_state.page == "main":
    st.markdown(
        dedent(
            """
            <div class="app-card">
                <div class="emoji">👋</div>
                <h1 class="title">안녕하세요</h1>
                <p class="subtitle">Streamlit으로 만든 첫 번째 간단한 웹앱입니다.</p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    st.button("나도 인사하기", on_click=go_greeting)

else:
    st.markdown(
        dedent(
            """
            <div class="app-card">
                <div class="fireworks" aria-hidden="true">
                    <span class="spark" style="--left:50%; --top:55%; --x:0px; --y:-95px; --delay:0s; --color:oklch(0.78 0.18 35);"></span>
                    <span class="spark" style="--left:50%; --top:55%; --x:65px; --y:-70px; --delay:0s; --color:oklch(0.82 0.16 80);"></span>
                    <span class="spark" style="--left:50%; --top:55%; --x:92px; --y:-5px; --delay:0s; --color:oklch(0.72 0.2 255);"></span>
                    <span class="spark" style="--left:50%; --top:55%; --x:54px; --y:62px; --delay:0s; --color:oklch(0.76 0.18 145);"></span>
                    <span class="spark" style="--left:50%; --top:55%; --x:-2px; --y:88px; --delay:0s; --color:oklch(0.72 0.2 305);"></span>
                    <span class="spark" style="--left:50%; --top:55%; --x:-62px; --y:54px; --delay:0s; --color:oklch(0.8 0.17 25);"></span>
                    <span class="spark" style="--left:50%; --top:55%; --x:-94px; --y:-6px; --delay:0s; --color:oklch(0.7 0.18 230);"></span>
                    <span class="spark" style="--left:50%; --top:55%; --x:-58px; --y:-72px; --delay:0s; --color:oklch(0.84 0.14 95);"></span>

                    <span class="spark" style="--left:26%; --top:42%; --x:0px; --y:-75px; --delay:0.35s; --color:oklch(0.75 0.2 310);"></span>
                    <span class="spark" style="--left:26%; --top:42%; --x:62px; --y:-28px; --delay:0.35s; --color:oklch(0.82 0.16 120);"></span>
                    <span class="spark" style="--left:26%; --top:42%; --x:38px; --y:54px; --delay:0.35s; --color:oklch(0.78 0.18 55);"></span>
                    <span class="spark" style="--left:26%; --top:42%; --x:-45px; --y:48px; --delay:0.35s; --color:oklch(0.7 0.18 250);"></span>
                    <span class="spark" style="--left:26%; --top:42%; --x:-68px; --y:-30px; --delay:0.35s; --color:oklch(0.78 0.17 20);"></span>

                    <span class="spark" style="--left:74%; --top:40%; --x:0px; --y:-78px; --delay:0.7s; --color:oklch(0.82 0.15 90);"></span>
                    <span class="spark" style="--left:74%; --top:40%; --x:66px; --y:-18px; --delay:0.7s; --color:oklch(0.74 0.2 285);"></span>
                    <span class="spark" style="--left:74%; --top:40%; --x:36px; --y:56px; --delay:0.7s; --color:oklch(0.76 0.18 150);"></span>
                    <span class="spark" style="--left:74%; --top:40%; --x:-40px; --y:54px; --delay:0.7s; --color:oklch(0.72 0.18 240);"></span>
                    <span class="spark" style="--left:74%; --top:40%; --x:-70px; --y:-22px; --delay:0.7s; --color:oklch(0.8 0.17 35);"></span>
                </div>

                <div class="emoji">🎉</div>
                <h1 class="title">첫 웹페이지 제작을 축하해요</h1>
                <p class="subtitle">버튼 클릭으로 화면 전환과 애니메이션까지 완성했습니다.</p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    st.button("돌아가기", on_click=go_main)
