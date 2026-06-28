import sqlite3
from pathlib import Path

DB_PATH = Path("data/dashboard.db")


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)

    return sqlite3.connect(DB_PATH)


def initialize_database():

    conn = get_connection()
    cur = conn.cursor()

    # ---------------- GPU ---------------- #

    cur.execute("""
    CREATE TABLE IF NOT EXISTS gpu_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

        gpu INTEGER,

        name TEXT,

        memory_used REAL,

        memory_total REAL,

        gpu_util REAL,

        memory_util REAL,

        temperature REAL,

        power REAL

    )
    """)

    # ---------------- CPU ---------------- #

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cpu_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

        cpu_percent REAL,

        ram_used REAL,

        ram_total REAL,

        ram_percent REAL

    )
    """)

    # ---------------- Storage ---------------- #

    cur.execute("""
    CREATE TABLE IF NOT EXISTS storage_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

        mount TEXT,

        total REAL,

        used REAL,

        free REAL,

        percent REAL

    )
    """)

    # ---------------- GPU Processes ---------------- #

    cur.execute("""
    CREATE TABLE IF NOT EXISTS gpu_process_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

        student TEXT,

        gpu INTEGER,

        pid INTEGER,

        gpu_memory REAL,

        cpu REAL,

        ram REAL,

        executable TEXT,

        working_directory TEXT,

        command TEXT

    )
    """)

    # ---------------- Notebooks ---------------- #

    cur.execute("""
    CREATE TABLE IF NOT EXISTS notebook_history (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

        kernel_id TEXT,

        notebook TEXT,

        student TEXT,

        pid INTEGER

    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":

    initialize_database()

    print("Dashboard database created successfully.")