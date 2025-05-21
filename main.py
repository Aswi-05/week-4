import os
import logging

# ✅ Ensure 'logs/' folder exists
os.makedirs('logs', exist_ok=True)

# ✅ Set up logging
logging.basicConfig(filename='logs/workout.log', level=logging.INFO)

from db import init_db, save_workout, fetch_history
from report import generate_report
import logging

logging.basicConfig(filename='logs/workout.log', level=logging.INFO)

def add_workout():
    try:
        workout_type = input("Workout Type: ")
        duration = float(input("Duration (minutes): "))
        calories = float(input("Calories Burned: "))
        date = input("Date (YYYY-MM-DD): ")
        save_workout(workout_type, duration, calories, date)
        logging.info(f"Workout added: {workout_type}, {duration} min, {calories} cal, {date}")
    except ValueError:
        print("❌ Invalid input.")

def view_history():
    history = fetch_history()
    print("\nWorkout History:")
    for row in history:
        print(row)

def suggest_improvements():
    history = fetch_history()
    if len(history) < 2:
        print("Not enough data.")
        return
    avg = sum([row[3] for row in history]) / len(history)
    print(f"✅ Your average calories burned: {avg:.2f}")
    print("💡 Try increasing duration for better results!")

def main():
    init_db()
    while True:
        print("\n🏋️ Workout Tracker 🏋️")
        print("1. Add Workout")
        print("2. View History")
        print("3. Suggestions")
        print("4. Generate Report")
        print("5. Exit")
        choice = input("Choice: ")

        if choice == '1':
            add_workout()
        elif choice == '2':
            view_history()
        elif choice == '3':
            suggest_improvements()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
