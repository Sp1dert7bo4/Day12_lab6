import urllib.request
import json
import os

# Read API Key from .env
api_key = ""
with open(".env", "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("AGENT_API_KEY="):
            api_key = line.strip().split("=")[1]

# Prepare request
url = "http://localhost:8000/ask"
headers = {
    "X-API-Key": api_key,
    "Content-Type": "application/json"
}
data = json.dumps({"question": "Bạn có thể làm được gì?"}).encode("utf-8")

# Send request
req = urllib.request.Request(url, data=data, headers=headers, method="POST")
try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())
        print("Trạng thái:", response.status)
        print("Phản hồi từ AI:", json.dumps(result, indent=2, ensure_ascii=False))
except urllib.error.HTTPError as e:
    print(f"Lỗi: {e.code} - {e.read().decode()}")
