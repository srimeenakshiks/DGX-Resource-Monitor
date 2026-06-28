import pandas as pd
import plotly.express as px

from gpu import get_gpu_info
from history import add_snapshot, get_history


def gpu_memory_chart():

    df = pd.DataFrame(get_gpu_info())

    fig = px.bar(
        df,
        x="GPU",
        y="Memory Used (GB)",
        color="GPU",
        text="Memory Used (GB)",
        title="GPU Memory Usage"
    )

    fig.update_layout(showlegend=False)

    return fig


def gpu_util_chart():

    df = pd.DataFrame(get_gpu_info())

    fig = px.bar(
        df,
        x="GPU",
        y="GPU Util (%)",
        color="GPU",
        text="GPU Util (%)",
        title="GPU Utilization"
    )

    fig.update_layout(showlegend=False)

    return fig


def history_chart():

    gpu_df = pd.DataFrame(get_gpu_info())

    add_snapshot(gpu_df)

    hist = pd.DataFrame(get_history())

    fig = px.line(
        hist,
        x="Time",
        y="Memory Used (GB)",
        color="GPU",
        markers=True,
        title="GPU Memory Over Time"
    )

    return fig