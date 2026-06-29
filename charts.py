"""
Interactive Plotly charts for DGX Monitor.
"""

import plotly.express as px

from analytics import (
    get_gpu_history,
    get_storage_history,
    get_top_gpu_users,
    get_gpu_hours_per_student,
    get_student_activity,
)

PLOT_BG = "#161b22"
PAPER_BG = "#0d1117"
FONT = "#f0f6fc"
GRID = "#30363d"


# ==========================================================
# Common Layout
# ==========================================================

def style(fig, title):

    fig.update_layout(

        title=title,

        template="plotly_dark",

        paper_bgcolor=PAPER_BG,

        plot_bgcolor=PLOT_BG,

        font_color=FONT,

        margin=dict(
            l=40,
            r=20,
            t=55,
            b=35,
        ),

        hovermode="x unified",

        legend=dict(
            orientation="h",
            y=1.05,
        ),

    )

    fig.update_xaxes(

        gridcolor=GRID

    )

    fig.update_yaxes(

        gridcolor=GRID

    )

    return fig


# ==========================================================
# GPU Utilization
# ==========================================================

def gpu_utilization_chart(hours=24):

    df = get_gpu_history(hours)

    fig = px.line(

        df,

        x="timestamp",

        y="gpu_util",

        color="gpu",

        markers=False,

    )

    return style(
        fig,
        f"GPU Utilization ({hours} Hours)"
    )


# ==========================================================
# GPU Memory
# ==========================================================

def gpu_memory_chart(hours=24):

    df = get_gpu_history(hours)

    fig = px.line(

        df,

        x="timestamp",

        y="memory_used",

        color="gpu",

    )

    return style(
        fig,
        f"GPU Memory Usage ({hours} Hours)"
    )


# ==========================================================
# Temperature
# ==========================================================

def temperature_chart(hours=24):

    df = get_gpu_history(hours)

    fig = px.line(

        df,

        x="timestamp",

        y="temperature",

        color="gpu",

    )

    return style(
        fig,
        "GPU Temperature"
    )


# ==========================================================
# Power
# ==========================================================

def power_chart(hours=24):

    df = get_gpu_history(hours)

    fig = px.line(

        df,

        x="timestamp",

        y="power",

        color="gpu",

    )

    return style(
        fig,
        "GPU Power Consumption"
    )


# ==========================================================
# Storage
# ==========================================================

def storage_chart():

    df = get_storage_history()

    df = df[df["mountpoint"] == "/lp-dev"]

    fig = px.line(

        df,

        x="timestamp",

        y="used",

        markers=True,

    )

    return style(
        fig,
        "/lp-dev Storage Growth"
    )


# ==========================================================
# GPU Hours
# ==========================================================

def gpu_hours_chart():

    df = get_gpu_hours_per_student()

    fig = px.bar(

        df,

        x="student",

        y="gpu_hours",

        text="gpu_hours",

    )

    fig.update_traces(
        textposition="outside"
    )

    return style(
        fig,
        "GPU Hours per Student"
    )


# ==========================================================
# Top GPU Users
# ==========================================================

def top_gpu_users_chart():

    df = get_top_gpu_users()

    fig = px.bar(

        df,

        x="student",

        y="avg_gpu_memory",

        text="avg_gpu_memory",

    )

    fig.update_traces(
        textposition="outside"
    )

    return style(
        fig,
        "Average GPU Memory Usage"
    )


# ==========================================================
# Notebook Activity
# ==========================================================

def notebook_activity_chart():

    df = get_student_activity()

    fig = px.bar(

        df,

        x="student",

        y="notebooks",

        text="notebooks",

    )

    fig.update_traces(
        textposition="outside"
    )

    return style(
        fig,
        "Notebook Activity"
    )