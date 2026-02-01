import csv
import os
import schedule
import time
from datetime import datetime
import matplotlib.pyplot as plt
from plyer import notification

FILENAME = "streak.csv"

def load_streak():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        return {rows[0]: rows[1] for rows in reader}

def save_streak(data):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        for date, status in data.items():
            writer.writerow([date, status])

def mark_today_solved():
    data = load_streak()
    today = datetime.utcnow().strftime("%Y-%m-%d")
    data[today] = "Solved"
    save_streak(data)
    print(f"✅ Marked {today} as Solved (UTC Date)")

def show_streak():
    data = load_streak()
    sorted_dates = sorted(data.keys())
    streak = []
    dates = []

    count = 0
    for d in sorted_dates:
        dates.append(d)
        if data[d] == "Solved":
            count += 1
        else:
            count = 0
        streak.append(count)

    plt.figure(figsize=(10, 4))
    plt.plot(dates, streak, marker='o')
    plt.title("LeetCode Streak Tracker (UTC)")
    plt.xlabel("Date")
    plt.ylabel("Current Streak")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def send_reminder():
    notification.notify(
        title="💡 LeetCode Reminder",
        message="Don't forget to solve a problem today! (Streak matters!)",
        timeout=10  # seconds
    )
    print("🔔 Reminder sent!")

def main_menu():
    while True:
        print("\n📅 LeetCode Streak Tracker")
        print("1. Mark Today as Solved")
        print("2. Show Streak Graph")
        print("3. Start Daily Reminder")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            mark_today_solved()
        elif choice == '2':
            show_streak()
        elif choice == '3':
            print("⏳ Reminder service started (press Ctrl+C to stop)...")
            schedule.every().day.at("21:30").do(send_reminder)  #  9:30 pm daily
            try:
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n🛑 Reminder stopped.")
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
