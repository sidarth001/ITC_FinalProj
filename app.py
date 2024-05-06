from flask import Flask, jsonify
import sqlite3
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return 'Welcome to the SQLite REST API'

@app.route('/users')
def get_users():
    try:
        conn = sqlite3.connect('userdata.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        conn.close()
        return jsonify(users)
    except Exception as e:
        logging.error(f"Error fetching users: {e}")
        return jsonify({'error': 'An error occurred while fetching users'}), 500

if __name__ == '__main__':
    app.run(debug=True)
