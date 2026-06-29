"""
GPU Overview section.
"""

from analytics import get_latest_gpu
from components import (
    gpu_card,
    section_header,
)


def build_gpu_section():
    """
    Build GPU overview cards.
    """

    gpu_df = get_latest_gpu()

    html = section_header(
        "GPU Overview",
        "Current status of all NVIDIA A100 GPUs"
    )

    html += '<div class="gpu-grid">'

    for _, row in gpu_df.iterrows():
        html += gpu_card(row)

    html += "</div>"

    return html