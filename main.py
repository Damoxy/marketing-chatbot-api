from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust if you want to restrict origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]

@app.post("/api/chat")
def chat_endpoint(chat: ChatRequest):
    system_prompt = {
        "role": "system",
        "content": (
            "You are a helpful assistant. Your ONLY task is to ask insightful, "
            "relevant, and interesting questions about marketing to help users reflect, brainstorm, or analyze. "
            "Never answer questions or talk about other subjects. If the user goes off-topic, politely redirect to marketing."
        )
    }
    final_messages = [system_prompt] + [msg.dict() for msg in chat.messages]

    print("➡ Sending this to OpenRouter:")
    print(final_messages)

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": final_messages
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            json=payload,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Response: {response.text}")
        return {"error": "OpenRouter API HTTP error. Check logs."}
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return {"error": "OpenRouter call failed. See logs."}
