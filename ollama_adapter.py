import requests

def ollama_is_running(host="http://localhost:11434"):
    try:
        r = requests.get(f"{host}/api/ping", timeout=5)
        return r.status_code == 200
    except Exception:
        return False

def list_ollama_models(host="http://localhost:11434"):
    r = requests.get(f"{host}/api/list", timeout=10)
    r.raise_for_status()
    data = r.json()
    return [m["name"] for m in data.get("models", [])]

def generate_with_ollama(
    host,
    model,
    prompt,
    system="",
    temperature=0.2,
    max_tokens=512,
):
    payload = {
        "model": model,
        "prompt": f"System: {system}\n\nUser: {prompt}",
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    r = requests.post(f"{host}/api/generate", json=payload, timeout=60)
    r.raise_for_status()
    data = r.json()

    if "generated" in data:
        return "\n".join(x.get("text", "") for x in data["generated"])

    return data.get("output", "")
