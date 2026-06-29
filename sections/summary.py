"""
Summary section.
"""

from analytics import (
    get_dashboard_summary,
    get_storage_growth,
)

from components import (
    metric_card,
    section_header,
)


def build_summary():

    summary = get_dashboard_summary()

    storage = get_storage_growth()

    storage_used = "--"

    if storage is not None:
        storage_used = f"{storage['current_used']:.0f} GB"

    html = section_header(
        "System Summary",
        "Current status of the DGX cluster"
    )

    html += '<div class="metric-grid">'

    html += metric_card(
        "GPUs",
        summary["gpus"]
    )

    html += metric_card(
        "Processes",
        summary["active_processes"]
    )

    html += metric_card(
        "Notebooks",
        summary["running_notebooks"]
    )

    html += metric_card(
        "Storage Used",
        storage_used
    )

    html += metric_card(
        "Storage Devices",
        summary["storage_devices"]
    )

    html += "</div>"

    return html