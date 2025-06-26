# together_api.py

from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")

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
