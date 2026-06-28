from datetime import datetime

history = []


def add_snapshot(df):

    global history

    now = datetime.now().strftime("%H:%M:%S")

    for _, row in df.iterrows():

        history.append({

            "Time": now,

            "GPU": row["GPU"],

            "GPU Util (%)": row["GPU Util (%)"],

            "Memory Used (GB)": row["Memory Used (GB)"]

        })


def get_history():

    return history