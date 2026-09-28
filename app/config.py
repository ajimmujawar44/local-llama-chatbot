import os


# ============================================================
# APPLICATION
# ============================================================

APP_TITLE = "Local LLaMA 3.2 AI Chatbot"

APP_ICON = "🤖"

AUTHOR = "Ajim Mujawar"


# ============================================================
# DOCKER MODEL RUNNER
# ============================================================

BASE_URL = os.getenv(
    "LLM_BASE_URL",
    "http://localhost:12434/engines/v1"
)

API_KEY = os.getenv(
    "LLM_API_KEY",
    "docker"
)

MODEL = os.getenv(
    "LLM_MODEL",
    "ai/llama3.2:1B-Q4_0"
)


# ============================================================
# MODEL SETTINGS
# ============================================================

DEFAULT_TEMPERATURE = 0.7

DEFAULT_MAX_TOKENS = 512


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    (
        "You are a helpful AI assistant. "
        "Provide clear, accurate, and easy-to-understand answers. "
        "Use examples when helpful. "
        "If you are unsure about something, clearly say so."
    )
)