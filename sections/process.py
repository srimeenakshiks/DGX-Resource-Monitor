"""
Live GPU Processes section.
"""

from analytics import get_latest_processes
from components import (
    section_header,
    process_card,
)


def build_process_section():

    df = get_latest_processes()

    html = section_header(
        "Running GPU Processes",
        "Live GPU compute jobs currently running",
        "process-section",
    )

    html += '<div class="process-grid">'

    if df.empty:

        html += """
        <div class="empty-card">
            No GPU processes detected.
        </div>
        """

    else:

        for _, row in df.iterrows():
            html += process_card(row)

    html += "</div>"

    return html