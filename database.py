import sqlite3
from pathlib import Path

DB_PATH = Path("data/dashboard.db")


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_database():

    conn = get_connection()
    cur = conn.cursor()

    # ==========================================================
    # GPU HISTORY
    # ==========================================================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS gpu_history (

        timestamp TEXT,

        gpu INTEGER,

        gpu_name TEXT,

        memory_used REAL,

        memory_total REAL,

        gpu_util REAL,

        memory_util REAL,

        temperature REAL,

        power REAL

    )
    """)

    # ==========================================================
    # PROCESS HISTORY
    # ==========================================================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS process_history (

        timestamp TEXT,

        gpu INTEGER,

        pid INTEGER,

        student TEXT,

        user TEXT,

        gpu_memory REAL,

        cpu REAL,

        ram REAL,

        executable TEXT,

        cwd TEXT,

        command TEXT

    )
    """)

    # ==========================================================
    # NOTEBOOK HISTORY
    # ==========================================================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS notebook_history (
    
        timestamp TEXT,
    
        kernel_id TEXT,
    
        pid INTEGER,
    
        student TEXT,
    
        notebook_name TEXT,
    
        kernel_name TEXT,
    
        cwd TEXT,
    
        status TEXT
    
    )
    """)

    # ==========================================================
    # STORAGE HISTORY
    # ==========================================================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS storage_history (

        timestamp TEXT,

        filesystem TEXT,

        total REAL,

        used REAL,

        available REAL,

        percent REAL,

        mountpoint TEXT

    )
    """)

    # ==========================================================
    # CPU HISTORY
    # ==========================================================

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cpu_history (

        timestamp TEXT,

        cpu_percent REAL,

        ram_percent REAL,

        ram_used REAL,

        ram_total REAL,

        swap_percent REAL,

        load1 REAL,

        load5 REAL,

        load15 REAL

    )
    """)

    conn.commit()
    conn.close()

    print("Database initialized.")


if __name__ == "__main__":
    initialize_database()