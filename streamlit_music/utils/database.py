# utils/database.py
import sqlite3
import os

def init_db():
    db_path = os.path.join(os.path.dirname(__file__), '../data/music_rating_app.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create tables
    c.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_type TEXT NOT NULL,
            item_name TEXT NOT NULL,
            votes INTEGER NOT NULL DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

def record_vote(item_type, item_name):
    db_path = os.path.join(os.path.dirname(__file__), '../data/music_rating_app.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''
        INSERT INTO votes (item_type, item_name, votes)
        VALUES (?, ?, 1)
        ON CONFLICT(item_type, item_name)
        DO UPDATE SET votes = votes + 1
    ''', (item_type, item_name))

    conn.commit()
    conn.close()

def get_winner(item_type):
    db_path = os.path.join(os.path.dirname(__file__), '../data/music_rating_app.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''
        SELECT item_name, MAX(votes)
        FROM votes
        WHERE item_type = ?
    ''', (item_type,))

    winner = c.fetchone()
    conn.close()

    return winner
