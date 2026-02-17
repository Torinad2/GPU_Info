# pip install gputil tabulate
# pip install setuptools

import GPUtil

from tabulate import tabulate
from typing import List, Tuple

def gpu_info() -> str:

    gpus = GPUtil.getGPUs()
    gpus_list: List[Tuple] = []

    for gpu in gpus:
        gpus_list.append((
        gpu.id,
        gpu.name,
        f"{gpu.load * 100:.1f}%",
        f"{gpu.memoryFree:.0f}MB",
        f"{gpu.memoryUsed}MB",
        f"{gpu.memoryTotal}MB",
        f"{gpu.temperature}°C"
        ))

    return tabulate(
        gpus_list,
        headers=["ID", "Name", "Load", "Free memory", "Used memory", "Total memory", "Temperature"],
        tablefmt="pretty"
    )

if __name__ == "__main__":
    print(gpu_info())