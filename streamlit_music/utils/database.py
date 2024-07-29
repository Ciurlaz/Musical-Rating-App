import os
import sqlite3
from datetime import datetime, timedelta

def init_db():
    # Assicurati che la cartella 'data/' esista
    if not os.path.exists('data'):
        os.makedirs('data')
    
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY,
                  username TEXT,
                  password TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS songs (
                  id INTEGER PRIMARY KEY,
                  title TEXT,
                  artist TEXT,
                  youtube_link TEXT,
                  favorite_parts TEXT,
                  lyrics TEXT,
                  user_id INTEGER,
                  songs_date_added DATE,
                  FOREIGN KEY(user_id) REFERENCES users(id)
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS albums (
                  id INTEGER PRIMARY KEY,
                  title TEXT,
                  artist TEXT,
                  link TEXT,
                  favorite_song TEXT,
                  songs_list TEXT,
                  user_id INTEGER,
                  albums_date_added DATE,
                  FOREIGN KEY(user_id) REFERENCES users(id)
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS ratings (
                  id INTEGER PRIMARY KEY,
                  user_id INTEGER,
                  item_id INTEGER,
                  rating REAL,
                  type TEXT,
                  user_date_added DATE,
                  FOREIGN KEY(user_id) REFERENCES users(id)
                )''')
    conn.commit()
    conn.close()


def add_song(title, artist, youtube_link, favorite_parts, lyrics, user_id):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute('INSERT INTO songs (title, artist, youtube_link, favorite_parts, lyrics, user_id, songs_date_added) VALUES (?, ?, ?, ?, ?, ?, ?)',
              (title, artist, youtube_link, favorite_parts, lyrics, user_id, datetime.now().date()))
    conn.commit()
    conn.close()

def add_album(title, artist, link, favorite_song, songs_list, user_id):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute('INSERT INTO albums (title, artist, link, favorite_song, songs_list, user_id, albums_date_added) VALUES (?, ?, ?, ?, ?, ?, ?)',
              (title, artist, link, favorite_song, songs_list, user_id, datetime.now().date()))
    conn.commit()
    conn.close()

def get_songs(date_filter="day"):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    today = datetime.now().date()
    if date_filter == "day":
        c.execute("SELECT * FROM songs WHERE songs_date_added = ?", (today,))
    elif date_filter == "week":
        start_week = today - timedelta(days=today.weekday())
        end_week = start_week + timedelta(days=6)
        c.execute("SELECT * FROM songs WHERE songs_date_added BETWEEN ? AND ?", (start_week, end_week))
    else:
        c.execute("SELECT * FROM songs")
    songs = [{'id': row[0], 'title': row[1], 'artist': row[2], 'youtube_link': row[3], 'favorite_parts': row[4], 'lyrics': row[5], 'user_id': row[6], 'songs_date_added': row[7]} for row in c.fetchall()]
    conn.close()
    return songs

def get_albums(date_filter="day"):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    today = datetime.now().date()
    if date_filter == "day":
        c.execute("SELECT * FROM albums WHERE albums_date_added = ?", (today,))
    elif date_filter == "week":
        start_week = today - timedelta(days=today.weekday())
        end_week = start_week + timedelta(days=6)
        c.execute("SELECT * FROM albums WHERE albums_date_added BETWEEN ? AND ?", (start_week, end_week))
    else:
        c.execute("SELECT * FROM albums")
    albums = [{'id': row[0], 'title': row[1], 'artist': row[2], 'link': row[3], 'favorite_song': row[4], 'songs_list': row[5], 'user_id': row[6], 'albums_date_added': row[7]} for row in c.fetchall()]
    conn.close()
    return albums

def get_ratings(item_type, date_filter):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    
    if item_type == "song":
        query = """
        SELECT s.id, s.title, s.artist, AVG(r.rating) AS average_rating
        FROM songs s
        JOIN ratings r ON s.id = r.song_id
        WHERE r.added_on BETWEEN ? AND ?  -- Usa il nome corretto della colonna
        GROUP BY s.id
        """
    elif item_type == "album":
        query = """
        SELECT a.id, a.title, a.artist, AVG(r.rating) AS average_rating
        FROM albums a
        JOIN ratings r ON a.id = r.album_id
        WHERE r.added_on BETWEEN ? AND ?  -- Usa il nome corretto della colonna
        GROUP BY a.id
        """
    else:
        return []
    
    c.execute(query, (date_filter, date_filter))
    rows = c.fetchall()
    conn.close()
    
    return [{'id': row[0], 'title': row[1], 'artist': row[2], 'average_rating': row[3]} for row in rows]



def add_rating(item_id, item_type, rating, user_id):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute('INSERT INTO ratings (item_id, item_type, rating, user_id) VALUES (?, ?, ?, ?)',
              (item_id, item_type, rating, user_id))
    conn.commit()
    conn.close()
