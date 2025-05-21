import sqlite3

def init_db():
    conn = sqlite3.connect("workout_data.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY,
                type TEXT,
                duration REAL,
                calories REAL,
                date TEXT)''')
    conn.commit()
    conn.close()

def save_workout(wtype, duration, calories, date):
    conn = sqlite3.connect("workout_data.db")
    c = conn.cursor()
    c.execute("INSERT INTO workouts (type, duration, calories, date) VALUES (?, ?, ?, ?)",
              (wtype, duration, calories, date))
    conn.commit()
    conn.close()

def fetch_history():
    conn = sqlite3.connect("workout_data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM workouts")
    rows = c.fetchall()
    conn.close()
    return rows
