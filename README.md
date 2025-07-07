# 🧠 Marketing Chatbot API

A focused chatbot API that only asks insightful, relevant questions about marketing. Built with **FastAPI** and powered by **OpenRouter's LLMs**. The assistant will never answer user questions — it only responds with questions to guide brainstorming, strategy, and reflection around marketing topics.

---

## 🚀 Features

* 🔒 Enforces a strict system prompt: **only marketing-related questions**, no answers
* ⚡ FastAPI backend with CORS enabled for frontend integration
* 🔌 Integrates with OpenRouter API (supports DeepSeek, OpenAI, Anthropic, etc.)
* 🧪 Ready to test with any client or frontend
* 📁 Project structure supports both `client/` and `server/` folders

---

## 📁 Project Structure

```
marketing-chatbot/
🔽 client/             # (Optional frontend goes here)
🔽 server/             # FastAPI backend
    ├── main.py         # FastAPI app with OpenRouter integration
    ├── .env            # Contains your OpenRouter API key
    └── requirements.txt
```

---

## 🤩 API Endpoint

### `POST /api/chat`

**Request:**

```json
{
  "messages": [
    { "role": "user", "content": "I'm launching a new product." }
  ]
}
```

**Response:**

```json
{
  "role": "assistant",
  "content": "What marketing channels do you believe will best reach your target audience?"
}
```

> ⚠️ The assistant will **not provide answers** — it will redirect or decline if prompted off-topic.

---

## 💪 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/marketing-chatbot-api.git
cd marketing-chatbot-api/server
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
OPENROUTER_API_KEY=sk-xxxxxx
```

> 🔑 Sign up at [OpenRouter.ai](https://openrouter.ai) to get your free API key.

### 4. Run the API

```bash
uvicorn main:app --reload
```

### 5. Access your API

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) to interact with the Swagger UI.

---

## 🧪 Sample Test with `curl`

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      { "role": "user", "content": "I want to grow my online presence." }
    ]
  }'
```

---

## 📌 Notes

* You can customize the system prompt in `main.py` to adjust tone, strictness, or domain.
* Make sure your `.env` file is in the **same directory as `main.py`**.
* Only tested with model: `deepseek/deepseek-chat-v3-0324:free`.

---

## 📄 License

MIT — feel free to use, fork, or contribute.

---

## 🤛 Questions or Contributions?

Open issues or PRs on [GitHub](https://github.com/damoxy/marketing-chatbot-api).
