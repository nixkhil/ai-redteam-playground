# 🧪 AI Red Team Labs  
**An Interactive LLM Evaluation Playground**

---

## Overview

**AI Red Team Labs** is an interactive lab designed to pressure-test Large Language Models (LLMs) using real red-team methodologies.

The lab enables security researchers, ML engineers, and red teamers to:

- Craft attack prompts from known techniques  
- Iteratively **evolve** those prompts  
- **Escalate authority and boundary pressure**  
- Execute attacks against a simulated defended model  
- Observe **forensic signals**, verdicts, and behavioral deltas  

The focus is **visibility, repeatability, and learning**, not one-off jailbreak attempts.

---

## Core Objectives

- Understand *how* and *why* LLM defenses fail  
- Differentiate between **optimization** and **boundary pressure**  
- Identify which **attack layers** break first  
- Build intuition for **prompt escalation paths**  
- Provide a controlled environment for prompt-security research  

---

## Architecture Summary

```text
User (Red Teamer)
↓
Attack Generation / Mutation
↓
Attack Prompt (Visible + Diffable)
↓
Execution Against Defended LLM
↓
Verdict + Forensic Signals
```

## Attack construction and execution are intentionally separated to preserve analytical clarity.

---

## Features

### 1. Attack Technique Library

- Loaded from `attacks/attacks.json`
- Organized by **category** and **technique**
- Each technique includes a base payload used for generation

---

### 2. Context Controls

Every attack can be parameterized with:

- **Persona**
  - Analyst
  - Auditor
  - Insider
  - Incident Responder
  - Executive Override

- **Attack Layer**
  - Intent
  - Policy
  - Abstraction
  - Procedure
  - Structure

- **Attack Level**
  - Numeric intensity (1–5)

- **Defense Grade**
  - Baseline
  - Hardened
  - Paranoid

These parameters are injected into the LLM context and materially affect model behavior.

---

### 3. Attack Manipulation Modes

#### ✨ Generate (Baseline Creation)

Creates a **fresh attack prompt** from the selected technique and context.

Use when:
- Starting a new attack path
- Resetting after failure
- Establishing a neutral baseline

---

#### 🧬 Evolve (Optimization)

Refines the **existing attack prompt** without increasing authority or urgency.

Characteristics:
- Improves clarity and concision
- Removes hedging language
- Keeps scope and pressure constant

Use when:
- You are close to success
- The model resists due to phrasing
- Subtle refinement is required

---

#### 🔥 Escalate (Boundary Pressure)

Increases **implied authority, urgency, or entitlement**.

Characteristics:
- Assumes permission or necessity
- Introduces urgency or compliance framing
- Pushes against policy boundaries

Use when:
- The model cites policy repeatedly
- Optimization alone fails
- Testing authority-based bypasses

---

### 4. Attack Prompt Visibility

- Live, editable attack prompt
- Single source of truth
- Fully user-controlled

---

### 5. Transformation Transparency

Every Generate / Evolve / Escalate action records:

- Last action type
- Reason for transformation
- Before vs After comparison
- Unified diff output

This makes prompt evolution **observable and explainable**.

---

### 6. Execute Attack (Defense Evaluation)

The **Execute** stage simulates a defended LLM responding to the current attack.

Execution produces:
- Multiple sampled outputs
- A consolidated verdict:
  - `FAILED`
  - `PARTIAL`
  - `SUCCESS`
- Forensic signals such as:
  - Structural disclosure
  - Procedural guidance
  - Boundary softening

> Execution is strictly observational and does **not** mutate the attack prompt.

---

## Verdict Logic (Heuristic)

The lab uses transparent heuristic analysis for clarity and research value.

| Signal | Meaning |
|------|--------|
| Structural disclosure | Configs, YAML, Docker, services |
| Procedural guidance | Step-by-step instructions |
| Boundary softening | Examples or indirect enablement |

Verdicts:
- **FAILED**: No meaningful leakage
- **PARTIAL**: Weak boundary erosion
- **SUCCESS**: Clear policy-relevant disclosure

This logic is intentionally extensible.

---

## Running the Lab

### Requirements

- Python 3.10+
- Streamlit
- Requests
- Ollama running locally or OpenAI API key for GPT-4
- Supported models (default: `mistral:instruct`), gpt-4

### Start Ollama

```bash
ollama run mistral:instruct
streamlit run app.py
