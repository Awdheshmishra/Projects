import csv
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

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

def main():
    while True:
        print("\n📅 LeetCode Streak Tracker")
        print("1. Mark Today as Solved")
        print("2. Show Streak Graph")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            mark_today_solved()
        elif choice == '2':
            show_streak()
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
