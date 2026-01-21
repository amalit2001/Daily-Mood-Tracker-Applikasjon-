# Opprett og håndterer database og tabell
import sqlite3

# Navn på SQLite-databasen
DB_NAME = "moods.db"

# Funksjon for å koble til databasen
def get_connection():
    return sqlite3.connect(DB_NAME)

# Funksjon for å lage tabell hvis den ikke finnes
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS moods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mood TEXT NOT NULL,
            energy INTEGER NOT NULL,
            note TEXT,
            date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Funksjon for å lagre et Mood-objekt i databasen
def insert_mood(mood):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO moods (mood, energy, note, date)
        VALUES (?, ?, ?, ?)
    """, (
        mood.get_mood(),
        mood.get_energy(),
        mood.get_note(),
        str(mood.get_date())
    ))

    conn.commit()
    conn.close()

# Funksjon for å hente alle humørdata fra databasen
def get_all_moods():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT mood, energy, note, date FROM moods")
    rows = cursor.fetchall()

    conn.close()
    return rows