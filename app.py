import gradio as gr

from dashboard import create_dashboard
from styles import CSS

demo = create_dashboard()

if __name__ == "__main__":

    demo.launch(
        server_name="0.0.0.0",
        share=True,
        inbrowser=False,
        quiet=False,
        css=CSS,
    )