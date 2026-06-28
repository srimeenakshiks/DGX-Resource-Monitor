import gradio as gr
import pandas as pd

from gpu import get_gpu_info
from processes import get_gpu_processes
from jupyter_utils import get_running_kernels

from monitor import (
    gpu_memory_chart,
    gpu_util_chart,
    history_chart,
)

# ==========================================================
# Theme + CSS
# ==========================================================

theme = gr.themes.Soft(
    primary_hue="green",
    secondary_hue="gray",
    neutral_hue="slate",
)

CUSTOM_CSS = """
.gradio-container{
    max-width:1700px !important;
}

.metric{
    background:#161b22;
    border:1px solid #30363d;
    border-radius:15px;
    padding:18px;
    text-align:center;
}

.metric h1{
    margin:0;
    font-size:34px;
    color:#58a6ff;
}

.metric p{
    margin:6px;
    font-size:16px;
    color:#8b949e;
}
"""

# ==========================================================
# Refresh Function
# ==========================================================

def refresh():

    gpu_df = pd.DataFrame(get_gpu_info())
    process_df = pd.DataFrame(get_gpu_processes())
    notebook_df = pd.DataFrame(get_running_kernels())

    gpu_count = len(gpu_df)

    busy_gpu = int((gpu_df["GPU Util (%)"] > 0).sum())

    process_count = len(process_df)

    notebook_count = len(notebook_df)

    gpu_card = f"""
    <div class="metric">
        <h1>{gpu_count}</h1>
        <p>Total GPUs</p>
    </div>
    """

    busy_card = f"""
    <div class="metric">
        <h1>{busy_gpu}</h1>
        <p>Busy GPUs</p>
    </div>
    """

    process_card = f"""
    <div class="metric">
        <h1>{process_count}</h1>
        <p>GPU Processes</p>
    </div>
    """

    notebook_card = f"""
    <div class="metric">
        <h1>{notebook_count}</h1>
        <p>Running Notebooks</p>
    </div>
    """

    return (

        gpu_card,
        busy_card,
        process_card,
        notebook_card,

        gpu_df,
        process_df,
        notebook_df,

        gpu_memory_chart(),
        gpu_util_chart(),
        history_chart(),

    )

# ==========================================================
# UI
# ==========================================================

with gr.Blocks(
    title="GPU Dashboard",
    theme=theme,
    css=CUSTOM_CSS,
) as demo:

    gr.HTML(
        """
        <div style="text-align:center;padding:15px">
            <h1>🖥 GPU Server Dashboard</h1>
            <p>NVIDIA DGX A100 Resource Monitor</p>
        </div>
        """
    )

    refresh_btn = gr.Button(
        "🔄 Refresh Dashboard",
        variant="primary",
        size="lg",
    )

    # ======================================================
    # Summary Cards
    # ======================================================

    with gr.Row():

        gpu_card = gr.HTML()

        busy_card = gr.HTML()

        process_card = gr.HTML()

        notebook_card = gr.HTML()

    # ======================================================
    # Tabs
    # ======================================================

    with gr.Tabs():

        with gr.Tab("Overview"):

            gpu_table = gr.Dataframe(
                interactive=False,
                wrap=True,
                label="GPU Information",
            )

        with gr.Tab("Charts"):

            with gr.Row():

                gpu_memory = gr.Plot(label="GPU Memory")

                gpu_util = gr.Plot(label="GPU Utilization")

            gpu_history = gr.Plot(label="GPU Memory History")

        with gr.Tab("Processes"):

            process_table = gr.Dataframe(
                interactive=False,
                wrap=True,
                label="GPU Processes",
            )

        with gr.Tab("Notebooks"):

            notebook_table = gr.Dataframe(
                interactive=False,
                wrap=True,
                label="Running Notebooks",
            )

    # ======================================================
    # Refresh Button
    # ======================================================

    refresh_btn.click(

        refresh,

        outputs=[

            gpu_card,
            busy_card,
            process_card,
            notebook_card,

            gpu_table,
            process_table,
            notebook_table,

            gpu_memory,
            gpu_util,
            gpu_history,

        ],

    )

    # ======================================================
    # Initial Load
    # ======================================================

    demo.load(

        refresh,

        outputs=[

            gpu_card,
            busy_card,
            process_card,
            notebook_card,

            gpu_table,
            process_table,
            notebook_table,

            gpu_memory,
            gpu_util,
            gpu_history,

        ],

    )

    # ======================================================
    # Auto Refresh Every 2 Seconds
    # ======================================================

    timer = gr.Timer(2)

    timer.tick(

        refresh,

        outputs=[

            gpu_card,
            busy_card,
            process_card,
            notebook_card,

            gpu_table,
            process_table,
            notebook_table,

            gpu_memory,
            gpu_util,
            gpu_history,

        ],

    )