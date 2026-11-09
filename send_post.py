import os
import requests

TOKEN = os.environ["BALE_TOKEN"]

url = f"https://tapi.bale.ai/bot{TOKEN}/getMe"

response = requests.get(url, timeout=20)

print("Status:", response.status_code)
print("Response:", response.text)

response.raise_for_status()
