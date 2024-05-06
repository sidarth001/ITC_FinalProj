import sqlite3

def create_database():
    with sqlite3.connect('userdata_3.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activity_log (
                id INTEGER PRIMARY KEY,
                username TEXT,
                activity TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        # Commit the changes
        conn.commit()

def insert_users():
    users = [("admin1", "admin1"), ("admin2", "admin2"), ("admin3", "admin3"), ("admin4", "admin4"), ("admin5", "admin5")]
    with sqlite3.connect('userdata_3.db') as conn:
        cursor = conn.cursor()
        cursor.executemany('INSERT INTO users (username, password) VALUES (?, ?)', users)
        # Commit the changes
        conn.commit()

def log_activity(username, activity):
    with sqlite3.connect('userdata_3.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO activity_log (username, activity) VALUES (?, ?)', (username, activity))
        # Commit the changes
        conn.commit()
