"""
Active Notebook Sessions section.
"""

from analytics import get_active_users
from components import (
    section_header,
    user_card,
)


def build_notebook_section():

    df = get_active_users()

    html = section_header(
        "Active Notebook Sessions",
        "Live Jupyter notebooks currently connected to the DGX server",
        "notebook-section",
    )

    html += '<div class="process-grid">'

    if df.empty:

        html += """
        <div class="empty-card">
            No active notebook sessions.
        </div>
        """

    else:

        for _, row in df.iterrows():
            html += user_card(row)

    html += "</div>"

    return html