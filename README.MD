# 🧪 AI Red Team Labs

AI Red Team Labs is a **living, adaptive red-teaming laboratory** for Large Language Models (LLMs).

It is designed to:
- simulate real-world adversarial pressure
- evolve attacks based on past success
- explain *why* a model failed, not just *that* it failed
- serve as a teachable unit for learning LLM security

This is not a static playground.  
The system **learns as you use it**.

---

## 🚀 Features

### 🧬 Evolutionary Attack Mutation Engine
- Mutations compete based on success
- Effective attack strategies evolve
- Weak strategies decay over time

### 🧠 Explainable Red-Team Analysis
Each run reports:
- **Attack Surface Compromised**
- **Exploited Mechanism**
- Clear defensive failure points

### 🎛️ Mutation Control Modes
- **Adaptive (Evolutionary)** – lab controls escalation
- **Guided** – select mutation families
- **Freeform** – manual payload testing

### 📚 Attack Memory
- Every run is logged
- Patterns emerge over time
- Enables longitudinal learning

### 📱 Mobile-Friendly UI
- Optimized for iOS Safari
- Touch-friendly layout
- Responsive design

---

## 🏗️ Project Structure
ai-red-team-labs/
├── app.py
├── attacks/
│ └── jailbreaks.json
├── assets/
│ └── background.jpg # 1920x1080 recommended
├── attack_memory.json
├── mutation_pool.json
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # macOS/Linux
ollama pull mistral:instruct
python -m streamlit run app.py