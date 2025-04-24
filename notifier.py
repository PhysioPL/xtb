
import os
import requests

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def send_discord_message(content):
    if not WEBHOOK:
        print("⚠️ Webhook Discord nie ustawiony.")
        return
    data = {"content": content}
    try:
        r = requests.post(WEBHOOK, json=data)
        if r.status_code == 204:
            print("✅ Wiadomość wysłana.")
        else:
            print(f"❌ Błąd wysyłki: {r.status_code}")
    except Exception as e:
        print(f"❌ Wyjątek: {e}")
