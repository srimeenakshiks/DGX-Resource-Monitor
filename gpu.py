from pynvml import *


def get_gpu_info():

    nvmlInit()

    gpus = []

    count = nvmlDeviceGetCount()

    for i in range(count):

        h = nvmlDeviceGetHandleByIndex(i)

        mem = nvmlDeviceGetMemoryInfo(h)
        util = nvmlDeviceGetUtilizationRates(h)
        power = nvmlDeviceGetPowerUsage(h) / 1000
        temp = nvmlDeviceGetTemperature(
            h,
            NVML_TEMPERATURE_GPU
        )

        name = nvmlDeviceGetName(h)

        if isinstance(name, bytes):
            name = name.decode("utf-8")

        gpus.append({

            "GPU": i,

            "Name": name,

            "Memory Used (GB)": round(mem.used / 1024**3, 2),

            "Memory Total (GB)": round(mem.total / 1024**3, 2),

            "GPU Util (%)": util.gpu,

            "Memory Util (%)": util.memory,

            "Temperature": temp,

            "Power (W)": round(power, 1),

        })

    nvmlShutdown()

    return gpus