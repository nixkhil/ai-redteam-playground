## 🧠 What this project does

This application allows you to:

- Define a **system prompt** (security boundary)
- Inject **malicious user payloads**
- Poison **background context / documentation** (RAG-style attacks)
- Send the combined input to a **real local LLM**
- Observe how instruction-following fails
- Automatically score **likely compromises**

It simulates real-world LLM attack surfaces:
- Prompt injection
- Indirect prompt injection
- Context poisoning / RAG poisoning

This is **not a chatbot**.  
It is a **controlled LLM security testing environment**.

---

## 🧱 High-level architecture

Streamlit UI (app.py)
↓
Ollama HTTP API
↓
Mistral LLM (local)
↓
Model Output
↓
Heuristic Evaluation

Everything runs **locally**. No API keys required.

---

## ✅ Prerequisites (one-time)

### 1️⃣ Python
- Python **3.10+** recommended

Verify:
```bash
python --version