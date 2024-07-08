import requests
import json
prompt = "What's the formula for energy?"

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "gemma:2b",
        "messages": [
            { "role": "user", "content": prompt}
        ],
        "temperature": 0,
    }
)

resp = response.content.decode("utf-8")
print(resp)
