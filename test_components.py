from analytics import get_latest_gpu
from analytics import get_latest_storage

from components import *

print(hero_header())

print(metric_card("GPUs", 8))

gpu = get_latest_gpu()

print(gpu_card(gpu.iloc[0]))

storage = get_latest_storage()

print(storage_card(storage.iloc[0]))

print(footer())
