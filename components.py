"""
Reusable UI components for DGX Monitor.

Every function here returns HTML that is rendered
inside Gradio HTML components.
"""

from datetime import datetime
from zoneinfo import ZoneInfo


# ==========================================================
# Header
# ==========================================================

def hero_header():

    now = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%d %b %Y • %H:%M:%S")

    return f"""
    <div class="hero">

        <div class="hero-title">
            DGX Resource Monitor
        </div>

        <div class="hero-subtitle">
            NVIDIA DGX A100 Multi-User Monitoring Platform
        </div>

        <div class="hero-status">

            <div class="live-chip">
                LIVE
            </div>

            <div class="time-chip">
                Updated: {now}
            </div>

        </div>

    </div>
    """


# ==========================================================
# Section Header
# ==========================================================

def section_header(title, subtitle="", section_id=None):

    anchor = ""

    if section_id:
        anchor = f'id="{section_id}"'

    return f"""
    <div class="section" {anchor}>

        <h2>{title}</h2>

        <p>{subtitle}</p>

    </div>
    """

# ==========================================================
# Summary Card
# ==========================================================

def metric_card(title, value, target=None):

    start = ""
    end = ""

    if target:

        start = f'<a href="#{target}" class="metric-link">'

        end = "</a>"

    return f"""

    {start}

    <div class="metric">

        <div class="metric-number">

            {value}

        </div>

        <div class="metric-label">

            {title}

        </div>

    </div>

    {end}

    """

# ==========================================================
# Status Chip
# ==========================================================

def status_chip(text, color="#2ea043"):

    return f"""
    <div
        style="
            display:inline-block;
            background:{color};
            color:white;
            padding:6px 14px;
            border-radius:999px;
            font-size:13px;
            font-weight:600;
        "
    >
        {text}
    </div>
    """


# ==========================================================
# Progress Bar
# ==========================================================

def progress_bar(percent):

    percent = max(0, min(percent, 100))

    if percent < 40:
        color = "#2ea043"

    elif percent < 75:
        color = "#d29922"

    else:
        color = "#f85149"

    return f"""
    <div class="progress">

        <div
            class="progress-fill"
            style="
                width:{percent}%;
                background:{color};
            "
        ></div>

    </div>
    """


# ==========================================================
# GPU Card
# ==========================================================

def gpu_card(row):

    util = float(row["gpu_util"])

    mem_percent = (
        row["memory_used"] /
        row["memory_total"]
    ) * 100

    return f"""

    <div class="gpu-card">

        <div class="gpu-title">

            GPU {int(row["gpu"])}

        </div>

        <div class="gpu-name">

            {row["gpu_name"]}

        </div>

        <b>GPU Utilization</b>

        {progress_bar(util)}

        <div class="gpu-row">

            <span>{util:.0f}%</span>

            <span>{row["temperature"]:.0f} °C</span>

        </div>

        <br>

        <b>Memory</b>

        {progress_bar(mem_percent)}

        <div class="gpu-row">

            <span>
                {row["memory_used"]:.2f} GB
            </span>

            <span>
                {row["memory_total"]:.0f} GB
            </span>

        </div>

        <div class="gpu-row">

            <span>Power</span>

            <b>{row["power"]:.0f} W</b>

        </div>

    </div>

    """

def user_card(row):

    student = row["student"] or "Unknown"

    status = row["status"].capitalize()

    color = "#2ea043"

    if status.lower() == "busy":
        color = "#d29922"

    elif status.lower() == "dead":
        color = "#f85149"

    gpu_text = "No GPU"

    if row["gpu_list"]:
        gpu_text = " • ".join(
            f"GPU {g}" for g in row["gpu_list"]
        )

    mem = row["gpu_memory"]
    mem_percent = min(mem / 80000 * 100, 100)

    cpu = row["cpu"]

    ram = row["ram"] / 1024

    notebook_html = ""

    for notebook in row["notebooks"]:
        notebook_html += f"""
        <div class="notebook-item">
            📓 {notebook}
        </div>
        """

    if not notebook_html:
        notebook_html = """
        <div class="notebook-item">
            None
        </div>
        """

    folder_html = ""

    for folder in row["folders"]:

        if len(folder) > 55:
            folder = "..." + folder[-52:]

        folder_html += f"""
        <div class="folder-item">
            📁 {folder}
        </div>
        """

    if not folder_html:
        folder_html = """
        <div class="folder-item">
            Unknown
        </div>
        """

    return f"""

    <div class="process-card">

        <div class="process-top">

            <div class="process-student">

                👤 {student}

            </div>

            {status_chip(status, color)}

        </div>

        <div class="gpu-row">

            <span>GPU</span>

            <b>{gpu_text}</b>

        </div>

        <br>

        <div class="label">

            GPU Memory

        </div>

        {progress_bar(mem_percent)}

        <div class="gpu-row">

            <span>{mem:.0f} MB</span>

        </div>

        <div class="gpu-row">

            <span>CPU</span>

            <b>{cpu:.1f}%</b>

        </div>

        <div class="gpu-row">

            <span>RAM</span>

            <b>{ram:.1f} GB</b>

        </div>

        <div class="gpu-row">

            <span>Kernel</span>

            <b>{row['kernel']}</b>

        </div>

        <br>

        <div class="section-label">

            Notebooks

        </div>

        {notebook_html}

        <br>

        <div class="section-label">

            Working Folders

        </div>

        {folder_html}

    </div>

    """

# ==========================================================
# Notebook Session Card
# ==========================================================

def notebook_card(row):

    student = row["student"] or "Unknown"

    status = row["status"].capitalize()

    notebooks = row["notebooks"]

    folders = row["folders"]

    notebook_html = ""

    if notebooks:

        for notebook in notebooks:

            notebook_html += f"""
            <div class="notebook-item">
                📓 {notebook}
            </div>
            """

    else:

        notebook_html = """
        <div class="notebook-item">
            No active notebooks
        </div>
        """

    folder_html = ""

    if folders:

        for folder in folders:

            if len(folder) > 55:
                folder = "..." + folder[-52:]

            folder_html += f"""
            <div class="folder-item">
                📁 {folder}
            </div>
            """

    else:

        folder_html = """
        <div class="folder-item">
            Unknown
        </div>
        """

    color = "#2ea043"

    if status.lower() == "busy":
        color = "#d29922"

    elif status.lower() == "dead":
        color = "#f85149"

    return f"""

    <div class="process-card">

        <div class="process-top">

            <div class="process-student">

                👤 {student}

            </div>

            {status_chip(status, color)}

        </div>

        <div class="section-label">

            Active Notebooks

        </div>

        {notebook_html}

        <div class="section-label">

            Working Directories

        </div>

        {folder_html}

    </div>

    """

# ==========================================================
# Storage Card
# ==========================================================

def storage_card(row):

    return f"""

    <div class="gpu-card">

        <div class="gpu-title">

            {row["mountpoint"]}

        </div>

        {progress_bar(row["percent"])}

        <div class="gpu-row">

            <span>Used</span>

            <b>{row["used"]:.0f} GB</b>

        </div>

        <div class="gpu-row">

            <span>Free</span>

            <b>{row["available"]:.0f} GB</b>

        </div>

        <div class="gpu-row">

            <span>Total</span>

            <b>{row["total"]:.0f} GB</b>

        </div>

    </div>

    """


# ==========================================================
# Footer
# ==========================================================

def footer():

    year = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).year

    return f"""

    <div class="footer">

        DGX Resource Monitor • Version 2.0

        <br><br>

        Built with ❤️ using Python, SQLite, Gradio & NVIDIA NVML

        <br><br>

        © {year}

    </div>

    """