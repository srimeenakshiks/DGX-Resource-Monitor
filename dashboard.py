"""
Dashboard layout.

This module assembles every dashboard section into
one reusable Gradio Blocks interface.
"""

import gradio as gr

from styles import CSS

from sections.header import build_header
from sections.summary import build_summary
from sections.gpu import build_gpu_section
from sections.process import build_process_section


def refresh_dashboard():

    return (
    
        build_header(),
    
        build_summary(),
    
        build_gpu_section(),
    
        build_process_section(),
    
    )

# ==========================================================
# Dashboard
# ==========================================================

def create_dashboard():

    with gr.Blocks(
        title="DGX Resource Monitor",
        fill_width=True,
    ) as demo:

        # --------------------------------------------------
        # Header
        # --------------------------------------------------

        header = gr.HTML(build_header())

        # --------------------------------------------------
        # Summary
        # --------------------------------------------------

        summary = gr.HTML(build_summary())

        # --------------------------------------------------
        # GPU Overview
        # --------------------------------------------------

        gpu_section = gr.HTML(build_gpu_section())

        # --------------------------------------------------
        # Analytics
        # --------------------------------------------------

        with gr.Group():

            gr.Markdown(
                "## Analytics"
            )

            analytics_placeholder = gr.Markdown(
                "_Coming soon..._"
            )

        # --------------------------------------------------
        # Storage
        # --------------------------------------------------

        with gr.Group():

            gr.Markdown(
                "## Storage"
            )

            storage_placeholder = gr.Markdown(
                "_Coming soon..._"
            )

        # --------------------------------------------------
        # Users
        # --------------------------------------------------

        with gr.Group():

            gr.Markdown(
                "## Users"
            )

            users_placeholder = gr.Markdown(
                "_Coming soon..._"
            )

        # --------------------------------------------------
        # Processes
        # --------------------------------------------------

        with gr.Group():

            gr.Markdown(
                "## Processes"
            )

            process_section = gr.HTML(
                build_process_section()
            )

        # --------------------------------------------------
        # Notebooks
        # --------------------------------------------------

        with gr.Group():

            gr.Markdown(
                "## Running Notebooks"
            )

            notebook_placeholder = gr.Markdown(
                "_Coming soon..._"
            )

        timer = gr.Timer(value=1)
        
        timer.tick(
            fn=refresh_dashboard,
            outputs=[
                header,
                summary,
                gpu_section,
                process_section,
            ],
        )
    
    return demo