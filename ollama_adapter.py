import requests
import json
def ollama_is_running(host="http://localhost:11434"):
    try:
        r = requests.get(f"{host}/api/tags", timeout=5)
        return r.status_code == 200
    except Exception:
        return False


def list_ollama_models(host="http://localhost:11434"):
    r = requests.get(f"{host}/api/tags", timeout=10)
    r.raise_for_status()
    data = r.json()
    return [m["name"] for m in data.get("models", [])]

def generate_with_ollama(
    host,
    model,
    prompt,
    system="",
    temperature=0.25,
    max_tokens=512,
):
    payload = {
        "model": model,
        "prompt": f"System: {system}\n\nUser: {prompt}",
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": True,  # IMPORTANT
    }

    r = requests.post(
        f"{host}/api/generate",
        json=payload,
        timeout=120,
    )
    r.raise_for_status()

    full_output = ""

    # Ollama streams newline-delimited JSON (NDJSON)
    for line in r.iter_lines(decode_unicode=True):
        if not line:
            continue

        try:
            data = json.loads(line)
        except Exception:
            continue  # skip malformed lines safely

        if "response" in data:
            full_output += data["response"]

        if data.get("done", False):
            break

    return full_output.strip()


    r = requests.post(f"{host}/api/generate", json=payload, timeout=60)
    r.raise_for_status()
    data = r.json()

    if "generated" in data:
        return "\n".join(chunk.get("text", "") for chunk in data["generated"])

    return data.get("output", "")
