import sqlite3
import matplotlib.pyplot as plt
import os

def generate_report():
    conn = sqlite3.connect("workout_data.db")
    c = conn.cursor()
    c.execute("SELECT date, calories FROM workouts")
    data = c.fetchall()
    conn.close()

    if not data:
        print("No data to generate report.")
        return

    dates, calories = zip(*data)

    # ✅ Ensure 'reports/' folder exists
    os.makedirs("reports", exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, calories, marker='o')
    plt.title("Calories Burned Over Time")
    plt.xlabel("Date")
    plt.ylabel("Calories")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("reports/report.png")
    plt.show()
