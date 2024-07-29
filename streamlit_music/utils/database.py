import sqlite3

# Funzione per creare le tabelle nel database (se non esistono già)
def create_tables():
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    
    # Creazione delle tabelle se non esistono già
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            date_added TEXT NOT NULL,
            uploaded_by INTEGER,
            FOREIGN KEY(uploaded_by) REFERENCES users(id)
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            date_added TEXT NOT NULL,
            uploaded_by INTEGER,
            FOREIGN KEY(uploaded_by) REFERENCES users(id)
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            FOREIGN KEY(item_id) REFERENCES songs(id),
            FOREIGN KEY(item_id) REFERENCES albums(id),
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()

# Funzione per ottenere le canzoni e le informazioni dell'utente che le ha caricate
def get_ratings(item_type, date_filter):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    
    if item_type == 'song':
        c.execute('''
            SELECT s.id, s.title, s.artist, s.date_added, u.username AS uploader
            FROM songs AS s
            JOIN users AS u ON s.uploaded_by = u.id
            WHERE s.date_added BETWEEN ? AND ?
        ''', date_filter)
    elif item_type == 'album':
        c.execute('''
            SELECT a.id, a.title, a.artist, a.date_added, u.username AS uploader
            FROM albums AS a
            JOIN users AS u ON a.uploaded_by = u.id
            WHERE a.date_added BETWEEN ? AND ?
        ''', date_filter)
    
    rows = c.fetchall()
    conn.close()
    
    return rows

# Funzione per registrare un voto
def vote_for_item(item_id, user_id, rating):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO ratings (item_id, user_id, rating)
        VALUES (?, ?, ?)
    ''', (item_id, user_id, rating))
    conn.commit()
    conn.close()

# Funzione per ottenere i dettagli di una canzone
def get_song_details(song_id):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute('''
        SELECT id, title, artist, date_added
        FROM songs
        WHERE id = ?
    ''', (song_id,))
    song = c.fetchone()
    conn.close()
    return song

# Funzione per ottenere i voti di una canzone
def get_song_votes(song_id):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute('''
        SELECT r.rating, u.username AS voter
        FROM ratings AS r
        JOIN users AS u ON r.user_id = u.id
        WHERE r.item_id = ? AND r.item_id IN (SELECT id FROM songs)
    ''', (song_id,))
    
    rows = c.fetchall()
    conn.close()
    
    return rows

# Funzione per ottenere i dettagli di un album
def get_album_details(album_id):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute('''
        SELECT id, title, artist, date_added
        FROM albums
        WHERE id = ?
    ''', (album_id,))
    album = c.fetchone()
    conn.close()
    return album

# Funzione per ottenere i voti di un album
def get_album_votes(album_id):
    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute('''
        SELECT r.rating, u.username AS voter
        FROM ratings AS r
        JOIN users AS u ON r.user_id = u.id
        WHERE r.item_id = ? AND r.item_id IN (SELECT id FROM albums)
    ''', (album_id,))
    
    rows = c.fetchall()
    conn.close()
    
    return rows

# Esegui la creazione delle tabelle
create_tables()
