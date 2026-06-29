import psutil


def get_storage_info():

    rows = []

    for part in psutil.disk_partitions(all=False):

        try:

            usage = psutil.disk_usage(part.mountpoint)

            rows.append({

                "Filesystem": part.device,

                "Total": round(usage.total / 1024**3, 2),

                "Used": round(usage.used / 1024**3, 2),

                "Available": round(usage.free / 1024**3, 2),

                "Percent": usage.percent,

                "Mountpoint": part.mountpoint,

            })

        except PermissionError:

            pass

    return rows