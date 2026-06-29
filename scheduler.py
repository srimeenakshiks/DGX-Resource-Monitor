import time
import logging

from collector import collect_once

logging.basicConfig(
    filename="logs/collector.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def run(interval=60):

    print(f"Collector running every {interval} seconds...")

    while True:

        try:

            collect_once()

        except Exception:

            logging.exception("Collector crashed.")

        time.sleep(interval)


if __name__ == "__main__":
    run()