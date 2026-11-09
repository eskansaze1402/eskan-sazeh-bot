import os
import requests

TOKEN = os.environ["BALE_TOKEN"]
CHANNEL = "@eskansazemehrespadana"

url = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHANNEL,
    "text": "🏗️ اسکان سازه مهر اسپادانا\n\nمهندسی رویای شما با ما\n\nفروش | اجاره | مشارکت در ساخت\n\nبه کانال ما خوش آمدید."
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.text)
