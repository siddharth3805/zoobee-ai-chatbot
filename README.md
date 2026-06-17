# 🐝 Zoobee — AI Chatbot with Memory

> A conversational AI chatbot built with Python and Streamlit that remembers your entire conversation, powered by Groq's free Llama 3.3 70B model.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red)
![Groq](https://img.shields.io/badge/LLM-Groq%20Llama%203.3-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 🔗 Live Demo

**[Try Zoobee live here →](PASTE_YOUR_STREAMLIT_URL_HERE)**

## 📖 Project Overview

Zoobee is a Generative AI chatbot built as part of the **Innovexa Catalyst Generative AI Internship (Batch 2026)**. It demonstrates core concepts of building production-ready conversational AI applications, including session-based memory, prompt engineering, and LLM API integration.

Unlike a simple Q&A bot, Zoobee maintains full conversational context — it remembers your name, previous questions, and earlier topics throughout a session, just like a real assistant would.

## ✨ Features

- 🧠 **Context-aware memory** — remembers up to 20 previous messages in the conversation
- ⚡ **Powered by Groq** — runs on Llama 3.3 70B with extremely fast inference speeds
- 🔄 **Rolling memory window** — automatically trims old messages to avoid token limit errors
- 💾 **Save chat history** — export conversations to JSON
- 🔒 **Secure API key management** via environment variables
- 📱 **Clean Streamlit UI** — responsive chat interface with sidebar controls
- 🆓 **100% free to run** — no billing or credit card required (Groq's free tier)

## 🔧 Tech Stack

- **Python 3.14** — Core language
- **Streamlit** — Web UI framework
- **Groq API (Llama 3.3 70B)** — LLM backend, free tier
- **python-dotenv** — Environment variable / API key management
- **In-Memory List** — Conversation history storage

## 📁 Project Structure

zoobee-ai-chatbot/
- app.py - Main Streamlit interface
- chatbot.py - Groq API integration
- memory.py - Conversation history management
- prompts.py - System prompt and personality
- utils.py - Helper functions
- requirements.txt - Python dependencies
- .env - API keys (not committed to git)
- .gitignore - Files excluded from version control
- README.md - This file

## 🚀 Getting Started Locally

### 1. Clone the repository
git clone https://github.com/siddharth3805/zoobee-ai-chatbot.git
cd zoobee-ai-chatbot

### 2. Create a virtual environment
python -m venv .venv
.venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up your Groq API key
Get a free API key at console.groq.com (no credit card needed), then create a `.env` file:
GROQ_API_KEY=your_groq_api_key_here

### 5. Run the app
streamlit run app.py
Open http://localhost:8501 in your browser.

## 🧩 How Memory Works

Zoobee stores the conversation as a list of message objects, sending the full history with every API call so the model maintains context. To prevent the history from growing indefinitely, only the last 20 messages are retained in a rolling window.

## ⚠️ Known Limitations

- Memory is session-based only — it resets when the app restarts
- Like any LLM, responses to highly specific factual questions may occasionally contain inaccuracies — always verify critical information independently
- Free-tier Groq rate limits apply (30 requests/minute, 14,400/day)

## 🏗️ Future Improvements

- Persistent storage with SQLite or JSON file-based memory across sessions
- Multi-user authentication
- RAG (Retrieval-Augmented Generation) for document Q&A
- Streaming responses for faster perceived speed

## 👤 Author

**Siddharth Balkrushana Sonawane**
GitHub: [@siddharth3805](https://github.com/siddharth3805)

---

*Built as part of the Innovexa Catalyst Generative AI Internship — Batch 2026* 🚀
