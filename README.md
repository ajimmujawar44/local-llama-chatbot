🤖 Local LLaMA 3.2 AI Chatbot

A local Generative AI chatbot built with Python, Streamlit, Docker Model Runner, and LLaMA 3.2.

The application provides a conversational interface for interacting with a locally running LLaMA model through an OpenAI-compatible API.

✨ Features

🤖 Local LLaMA 3.2 inference

🐳 Docker Model Runner integration

🎈 Interactive Streamlit chat interface

💬 Multi-turn conversation

⚡ Streaming responses

🌡️ Adjustable temperature

🔢 Adjustable maximum tokens

🗑️ Clear conversation

⚙️ Environment-based configuration

🧱 Docker and Docker Compose support

🧪 Standalone model connectivity test

🏗️ Architecture

User
  │
  ▼
Streamlit UI
  │
  ▼
LlamaClient + OpenAI SDK
  │
  │ OpenAI-compatible API
  ▼
Docker Model Runner
  │
  ▼
LLaMA 3.2 1B Q4_0

🛠️ Tech Stack

Technology

Purpose

Python

Application development

Streamlit

Chat interface

LLaMA 3.2

Local language model

Docker Model Runner

Local model inference

OpenAI Python SDK

API communication

Docker

Application containerization

Docker Compose

Container management

📁 Project Structure

local-llama-chatbot/
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── llm_client.py
│   └── ui.py
│
├── scripts/
│   └── test_model.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE

⚙️ Prerequisites

Install or enable:

Python 3.10+

Docker Desktop

Docker Model Runner

LLaMA 3.2 model

Verify Docker:

docker --version
docker run hello-world

Make sure the model is available:

ai/llama3.2:1B-Q4_0

🚀 Run Locally

1. Clone the repository

git clone <YOUR-GITHUB-REPOSITORY-URL>
cd local-llama-chatbot

2. Create and activate a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Test the model connection

python -m scripts.test_model

A successful connection should display:

CONNECTION SUCCESSFUL

5. Start the chatbot

streamlit run app/app.py

Open:

http://localhost:8501

🌡️ Temperature & Max Tokens

The sidebar provides two generation controls:

Setting

Controls

Temperature

Response randomness/creativity

Max Tokens

Maximum response length

Typical temperature values:

0.1 → More predictable
0.7 → Balanced
1.2 → More varied

🐳 Run with Docker

Build the image:

docker build -t local-llama-chatbot .

Run the application:

docker run -p 8501:8501 local-llama-chatbot

Open:

http://localhost:8501

🚀 Run with Docker Compose

docker compose up --build

Run in the background:

docker compose up --build -d

Stop the application:

docker compose down

⚙️ Configuration

The application supports environment variables:

LLM_MODEL=ai/llama3.2:1B-Q4_0
LLM_API_KEY=docker

When running Streamlit directly on Windows:

LLM_BASE_URL=http://localhost:12434/engines/v1

When running the Streamlit application inside Docker:

LLM_BASE_URL=http://host.docker.internal:12434/engines/v1

host.docker.internal allows the application container to communicate with Docker Model Runner on the host.

No real OpenAI API key is required for this local setup.

🔄 Application Flow

User enters prompt
        ↓
Streamlit receives message
        ↓
Conversation history
        ↓
LlamaClient
        ↓
Docker Model Runner
        ↓
LLaMA 3.2 generates response
        ↓
Response streams to Streamlit

🔐 Privacy

The application is designed for local LLM inference. Requests are sent to the locally running Docker Model Runner instead of requiring a cloud OpenAI API.

Privacy still depends on your local Docker configuration and any external services you add to the project.

🧠 What I Learned

Large Language Models and LLaMA

Prompting and system prompts

Conversation history and token generation

Temperature and response length

Streamlit session state and streaming

Modular Python application design

OpenAI-compatible APIs

Docker images, containers, and networking

Docker Compose

Host-to-container communication

📸 Screenshots

Add screenshots to a screenshots/ folder, for example:

screenshots/
├── dashboard.png
├── chat.png
└── docker-terminal.png

🎥 Demo

Add your project demonstration link here:

Demo: <http://localhost:8501>

🚧 Future Improvements

📄 PDF RAG

🔎 Vector database integration

💾 Persistent chat history

🎙️ Voice input

🔊 Text-to-speech

👥 Multiple model support

🔐 Authentication

📊 LLM monitoring

🧪 Automated testing

🚀 Production deployment

👨‍💻 Developer

Ajim Mujawar

Interests: Data Science • Machine Learning • Deep Learning • NLP • Generative AI • Agentic AI • LLM Applications • AI Engineering

📄 License

This project is licensed under the MIT License.