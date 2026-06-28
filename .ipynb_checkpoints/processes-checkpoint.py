import re
import psutil
from pynvml import *


def detect_student(path):
    """
    Detect student/research scholar ID from a path.
    """

    if not path:
        return "Unknown"

    patterns = [
        r"2[0-9]BRS\d+",
        r"2[0-9]BCE\d+",
        r"2[0-9]BLC\d+",
        r"2[0-9]PHD\d+",
    ]

    for pattern in patterns:
        match = re.search(pattern, path)
        if match:
            return match.group(0)

    return "Unknown"


def get_gpu_processes():

    nvmlInit()

    rows = []

    gpu_count = nvmlDeviceGetCount()

    for gpu in range(gpu_count):

        handle = nvmlDeviceGetHandleByIndex(gpu)

        try:
            gpu_processes = nvmlDeviceGetComputeRunningProcesses(handle)
        except Exception:
            gpu_processes = []

        for p in gpu_processes:

            pid = p.pid

            #
            # Defaults
            #
            cpu = 0
            ram = 0
            exe = ""
            cwd = ""
            cmd = ""
            username = "Unknown"

            try:

                proc = psutil.Process(pid)

                username = proc.username()

                cpu = proc.cpu_percent(interval=0.1)

                ram = proc.memory_info().rss / (1024 ** 2)

                exe = proc.exe()

                cwd = proc.cwd()

                cmd = " ".join(proc.cmdline())

            except Exception:
                pass

            #
            # Detect student
            #
            student = detect_student(cwd)

            #
            # If not found, also search executable
            #
            if student == "Unknown":
                student = detect_student(exe)

            #
            # If still not found, search command line
            #
            if student == "Unknown":
                student = detect_student(cmd)

            rows.append(
                {
                    "GPU": gpu,
                    "PID": pid,
                    "Student": student,
                    "GPU Memory (MB)": round(p.usedGpuMemory / (1024 ** 2), 1),
                    "CPU %": cpu,
                    "RAM (MB)": round(ram, 1),
                    "User": username,
                    "Executable": exe,
                    "Working Directory": cwd,
                    "Command": cmd,
                }
            )

    nvmlShutdown()

    return rows