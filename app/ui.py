import streamlit as st

from config import (
    AUTHOR,
    MODEL,
)


def render_sidebar():
    """Render the application sidebar."""

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
        # MODEL
        # ====================================================

        st.markdown("### 🧠 Model")

        st.code(
            MODEL,
            language="text",
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
                "Lower values make responses more predictable. "
                "Higher values make responses more creative."
            ),
        )

        max_tokens = st.slider(
            "Max Tokens",
            min_value=64,
            max_value=2048,
            value=512,
            step=64,
            help=(
                "Maximum number of tokens "
                "generated in the response."
            ),
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
        # DEVELOPER
        # ====================================================

        st.divider()

        st.markdown("### 👨‍💻 Developer")

        st.markdown(f"**{AUTHOR}**")

        st.caption(
            "Generative AI • LLM • Docker"
        )


    return temperature, max_tokens