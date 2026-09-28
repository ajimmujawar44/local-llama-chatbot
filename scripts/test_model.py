from openai import OpenAI
from app.config import API_KEY, BASE_URL, MODEL

print("=" * 60)
print("LOCAL LLAMA 3.2 MODEL TEST")
print("=" * 60)

print("Model:", MODEL)
print("Endpoint:", BASE_URL)
print()

client = OpenAI(
base_url=BASE_URL,
api_key=API_KEY
)

print("Connecting to Docker Model Runner...")

response = client.chat.completions.create(
model=MODEL,
messages=[
{
"role": "system",
"content": "You are a helpful AI assistant. Answer clearly and concisely."
},
{
"role": "user",
"content": "Explain what LLaMA 3.2 is in simple terms."
}
],
temperature=0.7,
max_tokens=200
)

answer = response.choices[0].message.content

print()
print("CONNECTION SUCCESSFUL")
print("-" * 60)
print("LLaMA Response:")
print()
print(answer)
print("-" * 60)