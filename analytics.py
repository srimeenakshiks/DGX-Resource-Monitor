import sqlite3
import pandas as pd

DB = "data/dashboard.db"


# ======================================================
# Database
# ======================================================

def query(sql, params=None):

    conn = sqlite3.connect(DB)

    try:
        return pd.read_sql_query(sql, conn, params=params)

    finally:
        conn.close()


# ======================================================
# Dashboard Summary
# ======================================================

def get_dashboard_summary():

    return {

        "gpus": int(query(
            "SELECT COUNT(DISTINCT gpu) AS n FROM gpu_history"
        )["n"].iloc[0]),

        "active_processes": int(query(
            """
            SELECT COUNT(*) AS n
            FROM process_history
            WHERE timestamp = (
                SELECT MAX(timestamp)
                FROM process_history
            )
            """
        )["n"].iloc[0]),

        "running_notebooks": int(query(
            """
            SELECT COUNT(*) AS n
            FROM notebook_history
            WHERE timestamp = (
                SELECT MAX(timestamp)
                FROM notebook_history
            )
            """
        )["n"].iloc[0]),

        "storage_devices": int(query(
            """
            SELECT COUNT(*) AS n
            FROM storage_history
            WHERE timestamp = (
                SELECT MAX(timestamp)
                FROM storage_history
            )
            """
        )["n"].iloc[0]),
    }


# ======================================================
# GPU
# ======================================================

def get_latest_gpu():

    return query("""

        SELECT *

        FROM gpu_history

        WHERE timestamp = (

            SELECT MAX(timestamp)

            FROM gpu_history

        )

        ORDER BY gpu

    """)


def get_gpu_history(hours=24):

    return query("""

        SELECT *

        FROM gpu_history

        WHERE timestamp >= datetime(
            'now',
            ?
        )

        ORDER BY timestamp

    """, [f"-{hours} hours"])


def get_average_gpu_util():

    return query("""

        SELECT

            gpu,

            ROUND(AVG(gpu_util),2) AS average_util

        FROM gpu_history

        GROUP BY gpu

        ORDER BY gpu

    """)


def get_peak_gpu_util():

    return query("""

        SELECT

            gpu,

            MAX(gpu_util) AS peak_util

        FROM gpu_history

        GROUP BY gpu

        ORDER BY gpu

    """)


def get_busiest_gpu():

    return query("""

        SELECT

            gpu,

            ROUND(AVG(gpu_util),2) AS average_util,

            MAX(gpu_util) AS peak_util,

            ROUND(AVG(memory_used),2) AS average_memory

        FROM gpu_history

        GROUP BY gpu

        ORDER BY average_util DESC

    """)


def get_peak_temperature():

    return query("""

        SELECT

            gpu,

            MAX(temperature) AS peak_temperature

        FROM gpu_history

        GROUP BY gpu

        ORDER BY gpu

    """)


def get_peak_power():

    return query("""

        SELECT

            gpu,

            MAX(power) AS peak_power

        FROM gpu_history

        GROUP BY gpu

        ORDER BY gpu

    """)


# ======================================================
# USERS
# ======================================================

def get_top_gpu_users(limit=10):

    return query("""

        SELECT

            student,

            COUNT(*) AS samples,

            ROUND(AVG(gpu_memory),2) AS avg_gpu_memory

        FROM process_history

        WHERE student IS NOT NULL
          AND student <> 'Unknown'

        GROUP BY student

        ORDER BY samples DESC

        LIMIT ?

    """, [limit])


def get_gpu_hours_per_student():

    df = query("""

        SELECT

            student,

            COUNT(*) AS samples

        FROM process_history

        WHERE student IS NOT NULL
          AND student <> 'Unknown'

        GROUP BY student

        ORDER BY samples DESC

    """)

    df["gpu_hours"] = (df["samples"] / 60).round(2)

    return df[
        [
            "student",
            "gpu_hours",
            "samples",
        ]
    ]


def get_top_memory_users(limit=10):

    return query("""

        SELECT

            student,

            ROUND(AVG(gpu_memory),2) AS avg_gpu_memory,

            MAX(gpu_memory) AS peak_gpu_memory

        FROM process_history

        WHERE student IS NOT NULL
          AND student <> 'Unknown'

        GROUP BY student

        ORDER BY avg_gpu_memory DESC

        LIMIT ?

    """, [limit])


# ======================================================
# STORAGE
# ======================================================

def get_latest_storage():

    return query("""

        SELECT *

        FROM storage_history

        WHERE timestamp=(

            SELECT MAX(timestamp)

            FROM storage_history

        )

    """)


def get_storage_history():

    return query("""

        SELECT *

        FROM storage_history

        ORDER BY timestamp

    """)


def get_storage_growth():

    df = get_storage_history()

    if len(df) < 2:

        return None

    growth = df["used"].iloc[-1] - df["used"].iloc[0]

    return {

        "growth_gb": round(growth, 2),

        "current_used": round(df["used"].iloc[-1], 2),

        "total": round(df["total"].iloc[-1], 2),

        "available": round(df["available"].iloc[-1], 2),

    }


# ======================================================
# NOTEBOOKS
# ======================================================

def get_running_notebooks():

    return query("""

        SELECT *

        FROM notebook_history

        WHERE timestamp=(

            SELECT MAX(timestamp)

            FROM notebook_history

        )

    """)


def get_student_activity():

    return query("""

        SELECT

            student,

            COUNT(*) AS notebooks

        FROM notebook_history

        WHERE student IS NOT NULL
          AND student <> 'Unknown'

        GROUP BY student

        ORDER BY notebooks DESC

    """)


# ======================================================
# HEALTH
# ======================================================

def get_health():

    gpu_avg = get_average_gpu_util()
    gpu_peak = get_peak_gpu_util()

    storage = get_storage_growth()
    
    return {
    
        "avg_gpu_util": round(
            gpu_avg["average_util"].mean(),
            2
        ),
    
        "peak_gpu_util": round(
            gpu_peak["peak_util"].max(),
            2
        ),
    
        "storage": storage,
    
    }

def get_latest_processes():

    return query("""

        SELECT *

        FROM process_history

        WHERE timestamp=(

            SELECT MAX(timestamp)

            FROM process_history

        )

        ORDER BY gpu

    """)

def get_gpu_count():

    return int(query("""

        SELECT COUNT(DISTINCT gpu) AS n

        FROM gpu_history

    """)["n"].iloc[0])

def get_latest_timestamp():

    return query("""

        SELECT MAX(timestamp) AS timestamp

        FROM gpu_history

    """)["timestamp"].iloc[0]

def get_database_stats():

    return {

        "gpu_rows": len(query(
            "SELECT * FROM gpu_history"
        )),

        "process_rows": len(query(
            "SELECT * FROM process_history"
        )),

        "notebook_rows": len(query(
            "SELECT * FROM notebook_history"
        )),

        "storage_rows": len(query(
            "SELECT * FROM storage_history"
        )),

    }

def get_latest_processes():

    return query("""

        SELECT *

        FROM process_history

        WHERE timestamp = (

            SELECT MAX(timestamp)

            FROM process_history

        )

        ORDER BY gpu

    """)

# ======================================================
# COMPLETE DASHBOARD DATA
# ======================================================

def get_dashboard_data():

    return {

        "summary": get_dashboard_summary(),

        "health": get_health(),

        "latest_gpu": get_latest_gpu(),

        "latest_processes": get_latest_processes(),

        "latest_storage": get_latest_storage(),

        "running_notebooks": get_running_notebooks(),

        "top_gpu_users": get_top_gpu_users(),

        "gpu_hours": get_gpu_hours_per_student(),

        "top_memory_users": get_top_memory_users(),

        "student_activity": get_student_activity(),

        "average_gpu_util": get_average_gpu_util(),

        "peak_gpu_util": get_peak_gpu_util(),

        "busiest_gpu": get_busiest_gpu(),

        "peak_temperature": get_peak_temperature(),

        "peak_power": get_peak_power(),

        "storage_history": get_storage_history(),

    }