
import schedule
import time
from signal_engine import analyze_market
from notifier import send_discord_message

def job():
    signals = analyze_market()
    for signal in signals:
        send_discord_message(signal)

schedule.every(10).minutes.do(job)

print("🤖 Bot KASSA uruchomiony. Oczekiwanie na sygnały...")
while True:
    schedule.run_pending()
    time.sleep(1)
