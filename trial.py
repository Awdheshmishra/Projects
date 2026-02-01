import requests
from bs4 import BeautifulSoup
from plyer import notification
import schedule
import time
from datetime import datetime

LEETCODE_USERNAME = "your_username"

def check_streak():
    url = f"https://leetcode.com/{LEETCODE_USERNAME}/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        data = soup.find("span", {"class": "text-label-1 dark:text-dark-label-1 font-medium"}).text
        print(f"Today’s solved count: {data}")

        if int(data) == 0:
            notification.notify(
                title="LeetCode Reminder",
                message="Aaj ka streak tod mat! Ek problem solve kar le 💻",
                timeout=10
            )
        else:
            print("Streak safe ✅")

    except Exception as e:
        print("Failed to parse profile data:", e)

# Roz 12:00 baje chalana
schedule.every().day.at("12:00").do(check_streak)

print("🕒 Streak Saver Running... Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
