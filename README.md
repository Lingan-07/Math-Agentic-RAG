<h1 align="center">🤖 Math Agentic RAG</h1>
<p align="center">
  <b>A Math Reasoning Agent powered by FastAPI + React</b><br/>
  <i>Built by Lingan — An AI-driven math solver with real-time reasoning and feedback.</i>
</p>

---

## ✨ Overview

**Math Agentic RAG** is an intelligent math problem-solving assistant that uses  
**Retrieval-Augmented Generation (RAG)** and **Agentic reasoning** to solve complex math queries,  
display step-by-step solutions, and interact in a clean ChatGPT-like interface.

---

## 🚀 Features

- 🧮 **Math Reasoning Engine** — Solves algebra, calculus, and geometry questions dynamically  
- 🔍 **Retrieval-Augmented Generation (RAG)** — Uses Qdrant vector store for contextual answers  
- 💬 **ChatGPT-like UI** — React-based conversational frontend with smart response layout  
- 📡 **FastAPI Backend** — Handles queries, routing, and reasoning seamlessly  
- 👍👎 **Feedback Storage System** — Saves user feedback for evaluation  
- 🌐 **Web Search Integration** (Tavily API) — Pulls external data for better answers  

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|-------------|
| 🎨 **Frontend** | React.js, Axios, CSS3 |
| ⚙️ **Backend** | FastAPI, Pydantic, Uvicorn |
| 🧠 **AI / ML** | LangChain, Sentence Transformers, Qdrant Client |
| 🗃️ **Database** | Qdrant Vector Store |
| ☁️ **Other Tools** | OpenAI / Tavily API, JSON-based feedback logs |

---

## 🧰 Setup Instructions

### 🖥️ Backend (FastAPI)
```bash
cd math_agent
pip install -r requirements.txt
uvicorn main:app --reload
