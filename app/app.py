
import streamlit as st

from config import (
    APP_TITLE,
    APP_ICON,
    MODEL,
    SYSTEM_PROMPT,
)
from llm_client import LlamaClient
from ui import render_sidebar


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="APP_TITLE",
    page_icon="APP_ICON",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = SYSTEM_PROMPT


# ============================================================
# HEADER
# ============================================================

st.title(f"{APP_ICON} {APP_TITLE}")

st.markdown(
    """
    **Private • Local • Docker-Powered Generative AI**

    Chat with **LLaMA 3.2** running locally through
    **Docker Model Runner** — no cloud AI API required.
    """
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

temperature, max_tokens = render_sidebar()


# ============================================================
# LLM CLIENT
# ============================================================

@st.cache_resource
def get_llm_client():
    return LlamaClient()


llm = get_llm_client()


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):

        if message["role"] == "user":
            st.markdown(message["content"])

        else:
            st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Ask LLaMA anything..."
)


if user_input:

    # --------------------------------------------------------
    # Add user message
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)


    # --------------------------------------------------------
    # Generate AI response
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        try:

            response_placeholder = st.empty()

            full_response = ""

            with st.spinner("🧠 LLaMA is thinking..."):

                for token in llm.stream_chat(
                    st.session_state.messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                ):

                    full_response += token

                    response_placeholder.markdown(
                        full_response + "▌"
                    )

            response_placeholder.markdown(
                full_response
            )


            # ------------------------------------------------
            # Save assistant response
            # ------------------------------------------------

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response,
                }
            )


        except Exception as error:

            st.error(
                "❌ Unable to connect to the local LLaMA model."
            )

            st.warning(
                "Please make sure Docker Model Runner is "
                "running and the LLaMA model is available."
            )

            with st.expander("Technical Details"):
                st.exception(error)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🤖 Local LLaMA 3.2 AI Chatbot  •  "
    "Built by Ajim Mujawar  •  "
    "Powered by Docker Model Runner"
)




import streamlit as st

from config import MODEL


def render_sidebar():
    """Render the chatbot sidebar."""

    with st.sidebar:

        # ====================================================
        # BRANDING
        # ====================================================

        st.markdown("## 🤖 LLaMA Chatbot")

        st.caption(
            "Local Generative AI Assistant"
        )

        st.divider()


        # ====================================================
        # MODEL INFORMATION
        # ====================================================

        st.markdown("### 🧠 Model")

        st.code(
            MODEL,
            language="text"
        )

        st.success("🟢 Local Model")


        # ====================================================
        # GENERATION SETTINGS
        # ====================================================

        st.markdown("### ⚙️ Generation Settings")

        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.5,
            value=0.7,
            step=0.1,
            help=(
                "Lower values produce more predictable responses. "
                "Higher values produce more creative responses."
            ),
        )

        max_tokens = st.slider(
            "Max Tokens",
            min_value=64,
            max_value=2048,
            value=512,
            step=64,
            help="Maximum length of the generated response.",
        )


        # ====================================================
        # CHAT CONTROLS
        # ====================================================

        st.divider()

        st.markdown("### 💬 Chat")

        if st.button(
            "🗑️ Clear Conversation",
            use_container_width=True,
        ):

            st.session_state.messages = [
                {
                    "role": "system",
                    "content": st.session_state.system_prompt,
                }
            ]

            st.rerun()


        # ====================================================
        # TECHNOLOGY
        # ====================================================

        st.divider()

        st.markdown("### 🛠️ Technology")

        st.caption("🐳 Docker Model Runner")
        st.caption("🦙 LLaMA 3.2")
        st.caption("🎈 Streamlit")
        st.caption("🐍 Python")
        st.caption("🔌 OpenAI-compatible API")


        # ====================================================
        # AUTHOR
        # ====================================================

        st.divider()

        st.markdown("### 👨‍💻 Developer")

        st.markdown("**Ajim Mujawar**")

        st.caption(
            "Generative AI • LLM • Docker"
        )


    return temperature, max_tokens


