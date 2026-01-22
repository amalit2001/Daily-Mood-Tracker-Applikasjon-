# Opprett og håndterer database og tabell
import sqlite3

# Navn på SQLite-databasen
DB_NAME = "moods.db"

# Funksjon for å koble til databasen
def connect_db():
    return sqlite3.connect(DB_NAME)

# Funksjon for å lage tabell hvis den ikke finnes
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Lager tabell om den ikke finnes fra før av
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mood_entries (
            entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
            mood_text TEXT NOT NULL,
            energy_level INTEGER NOT NULL,
            note_text TEXT,
            entry_date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Funksjon for å lagre et Mood-objekt i databasen
def save_mood_entry(mood):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO mood_entries (mood_text, energy_level, note_text, entry_date)
        VALUES (?, ?, ?, ?)
    """, (
        mood.get_mood(),
        mood.get_energy(),
        mood.get_note(),
        # Legger til dato og tid
        str(mood.get_datetime().strftime("%Y-%m-%d %H:%M"))
    ))

    conn.commit()
    conn.close()

# Funksjon for å hente alle humørdata fra databasen
def get_all_moods():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
     """SELECT mood_text, energy_level, note_text, entry_date
        FROM mood_entries
        ORDER BY entry_date DESC""")
    rows = cursor.fetchall()

    conn.close()
    return rows