#***************************************************************
# GPU Information Utility                                      *
# -------------------------------------------------------------*
# Description:                                                 *
#   Displays current GPU statistics including:                 *
#   - GPU ID                                                   *
#   - Name                                                     *
#   - Load (%)                                                 *
#   - Free / Used / Total Memory (MB)                          *
#   - Temperature (°C)                                         *
#                                                              *
#                                                              *
# Developed for learning system monitoring with Python.        *
#***************************************************************

# pip install gputil tabulate
# pip install setuptools

#=============================#
# Import Section              #
#=============================#

import GPUtil

from tabulate import tabulate
from typing import List, Tuple

#=============================#
# GPU Information Function    #
#=============================#

def gpu_info() -> str:
    """
    Retrieves GPU statistics and returns a formatted table string.
    """

    # Get list of detected GPUs
    gpus = GPUtil.getGPUs()

    # Prepare list for formatted output
    gpus_list: List[Tuple] = []

    # Loop through all detected GPUs
    for gpu in gpus:
        gpus_list.append((
        gpu.id,                     # GPU ID
        gpu.name,                   # Load percentage
        f"{gpu.load * 100:.1f}%",   # Load percentage
        f"{gpu.memoryFree:.0f}MB",  # Free memory
        f"{gpu.memoryUsed}MB",      # Used memory
        f"{gpu.memoryTotal}MB",     # Total memory
        f"{gpu.temperature}°C"      # Temperature
        ))

    # Return formatted table
    return tabulate(
        gpus_list,
        headers=["ID", "Name", "Load", "Free memory", "Used memory", "Total memory", "Temperature"],
        tablefmt="pretty"
    )

#=============================#
# Main Execution Section      #
#=============================#
if __name__ == "__main__":
    print(gpu_info())