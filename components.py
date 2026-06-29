"""
Reusable UI components for DGX Monitor.

Every function here returns HTML that is rendered
inside Gradio HTML components.
"""

from datetime import datetime


# ==========================================================
# Header
# ==========================================================

def hero_header():

    now = datetime.now().strftime("%d %b %Y • %H:%M:%S")

    return f"""
    <div class="hero">

        <div class="hero-title">
            🖥 DGX Resource Monitor
        </div>

        <div class="hero-subtitle">
            NVIDIA DGX A100 Multi-User Monitoring Platform
        </div>

        <div class="hero-status">

            <div class="live-chip">
                ● LIVE
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

def section_header(title, subtitle=""):

    return f"""
    <div class="section">

        <h2>{title}</h2>

        <p>{subtitle}</p>

    </div>
    """


# ==========================================================
# Summary Card
# ==========================================================

def metric_card(title, value):

    return f"""
    <div class="metric">

        <div class="metric-number">
            {value}
        </div>

        <div class="metric-label">
            {title}
        </div>

    </div>
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


# ==========================================================
# Storage Card
# ==========================================================

def storage_card(row):

    return f"""

    <div class="gpu-card">

        <div class="gpu-title">

            💾 {row["mountpoint"]}

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

    year = datetime.now().year

    return f"""

    <div class="footer">

        DGX Resource Monitor • Version 2.0

        <br><br>

        Built with ❤️ using Python, SQLite, Gradio & NVIDIA NVML

        <br><br>

        © {year}

    </div>

    """