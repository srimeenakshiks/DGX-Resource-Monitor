from datetime import datetime


def build_header(last_updated=None, status="LIVE"):
    """
    Builds the dashboard header.
    """

    if last_updated is None:
        last_updated = datetime.now().strftime("%d %b %Y • %H:%M:%S")

    status_class = "status-live"

    if status.upper() == "WARNING":
        status_class = "status-warning"

    elif status.upper() == "OFFLINE":
        status_class = "status-offline"

    return f"""
    <div class="hero">

        <div class="hero-left">

            <div class="hero-title">
                DGX Resource Monitor
            </div>

            <div class="hero-subtitle">
                NVIDIA DGX A100 Multi-User Compute Platform
            </div>

        </div>

        <div class="hero-right">

            <div class="{status_class}">
                {status}
            </div>

            <div class="hero-time">

                Last Updated

                <br>

                <b>{last_updated}</b>

            </div>

        </div>

    </div>
    """