import logging
import pandas as pd

from database import get_connection
from utils import timestamp

from gpu import get_gpu_info
from processes import get_gpu_processes
from storage import get_storage_info
from jupyter_utils import get_running_kernels


logging.basicConfig(
    filename="logs/collector.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def save_dataframe(df, table):
    """Append dataframe to SQLite."""

    if df.empty:
        return

    conn = get_connection()

    df.to_sql(
        table,
        conn,
        if_exists="append",
        index=False,
    )

    conn.close()


# =====================================================
# GPU
# =====================================================

def collect_gpu():

    df = pd.DataFrame(get_gpu_info())

    if df.empty:
        return

    df.insert(0, "timestamp", timestamp())

    df = df.rename(columns={
        "GPU": "gpu",
        "Name": "gpu_name",
        "Memory Used (GB)": "memory_used",
        "Memory Total (GB)": "memory_total",
        "GPU Util (%)": "gpu_util",
        "Memory Util (%)": "memory_util",
        "Temperature": "temperature",
        "Power (W)": "power",
        "Notebook Name": "notebook_name",
        "Kernel Name": "kernel_name",
    })

    save_dataframe(df, "gpu_history")


# =====================================================
# GPU Processes
# =====================================================

def collect_processes():

    df = pd.DataFrame(get_gpu_processes())

    if df.empty:
        return

    df.insert(0, "timestamp", timestamp())

    df = df.rename(columns={
        "GPU": "gpu",
        "PID": "pid",
        "Student": "student",
        "User": "user",
        "GPU Memory (MB)": "gpu_memory",
        "CPU %": "cpu",
        "RAM (MB)": "ram",
        "Executable": "executable",
        "Working Directory": "cwd",
        "Command": "command",
    })

    save_dataframe(df, "process_history")


# =====================================================
# Jupyter Notebooks
# =====================================================

from pathlib import Path

def collect_notebooks():

    df = pd.DataFrame(get_running_kernels())

    if df.empty:
        return

    df["student"] = df["Notebook"].apply(
        lambda x: Path(str(x)).parts[0] if "/" in str(x) else None
    )

    df["cwd"] = df["Notebook"].apply(
        lambda x: str(Path(str(x)).parent)
    )

    df["notebook_name"] = df["Notebook"].apply(
        lambda x: Path(str(x)).name
    )
    
    df["kernel_name"] = df["Kernel Name"]

    df["pid"] = None

    df = df.rename(columns={
        "Kernel ID": "kernel_id",
        "Execution State": "status",
    })

    df = df[
        [
            "kernel_id",
            "pid",
            "student",
            "notebook_name",
            "kernel_name",
            "cwd",
            "status",
        ]
    ]

    df.insert(0, "timestamp", timestamp())

    save_dataframe(df, "notebook_history")


# =====================================================
# Storage
# =====================================================

def collect_storage():

    df = pd.DataFrame(get_storage_info())

    if df.empty:
        return

    df.insert(0, "timestamp", timestamp())

    df = df.rename(columns={
        "Filesystem": "filesystem",
        "Total (GB)": "total",
        "Used (GB)": "used",
        "Available (GB)": "available",
        "Use %": "percent",
        "Mounted on": "mountpoint",
    })

    save_dataframe(df, "storage_history")


# =====================================================
# Master Collector
# =====================================================

def collect_once():

    logging.info("Starting collection...")

    try:
        collect_gpu()
        collect_processes()
        collect_notebooks()
        collect_storage()

        logging.info("Collection completed.")

        print("✓ Data collected")

    except Exception:

        logging.exception("Collector failed.")

        raise


if __name__ == "__main__":
    collect_once()