# together_api.py

import requests
import json

API_KEY = "f2f0eaaeba72d8e6cdabc2e6bc86d8b62c8362e7069479d5a77b931ae9cad339"  # Replace with your actual key

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def query_together_ai(prompt, max_tokens=100, temperature=0.7):
    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": 0.9
    }

    response = requests.post(
        "https://api.together.ai/v1/completions",
        headers=HEADERS,
        data=json.dumps(data)
    )

    try:
        result = response.json()
        if "choices" in result and result["choices"]:
            return result["choices"][0].get("text", "").strip()
        elif "error" in result:
            return f"[ERROR] {result['error']['message']}"
        else:
            return "[ERROR] Unexpected response format."
    except Exception as e:
        return f"[ERROR] Failed to parse response: {e}"
