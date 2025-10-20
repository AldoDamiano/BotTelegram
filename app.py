from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.getenv("8172892664:AAF-uQp6HP-_2HXu-MLR1uoLxTMi1qG4Lz0")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/')
def home():
    return "Bot Telegram attivo su Render!"

@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        send_message(chat_id, f"Ciao 👋 hai scritto: {text}")

    return {"ok": True}

def send_message(chat_id, text):
    url = f"{TELEGRAM_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
