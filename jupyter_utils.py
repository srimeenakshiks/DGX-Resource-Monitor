import os
import json
import glob
import requests


def get_running_kernels():

    runtime = os.path.expanduser("~/.local/share/jupyter/runtime")

    server_files = glob.glob(os.path.join(runtime, "jpserver-*.json"))

    rows = []

    for server in server_files:

        try:

            with open(server) as f:
                info = json.load(f)

            url = info["url"].rstrip("/")
            token = info.get("token", "")

            r = requests.get(
                f"{url}/api/sessions",
                params={"token": token},
                timeout=3,
            )

            if r.status_code != 200:
                continue

            sessions = r.json()

            for s in sessions:

                kernel = s["kernel"]

                notebook = s.get("notebook", {})
                path = notebook.get("path", "")
                notebook_name = os.path.basename(path) if path else ""

                rows.append({

                    "Kernel ID": kernel["id"],

                    "Kernel Name": kernel["name"],

                    "Execution State": kernel["execution_state"],

                    "Notebook": path,

                    "Notebook Name": notebook_name,

                    "Type": s.get("type", ""),

                })

        except Exception as e:
            print("Error:", e)

    return rows