import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

if __name__ == "__main__":
    numbers = [0, 5, 32, 64, 127, 255]
    voltages = [0.480, 0.480, 0.496, 0.817, 1.614, 3.232]
    assert (len (voltages) == len (numbers))

    figure (figsize=(14, 10), dpi=80)
    plt.plot (numbers, voltages, marker="*")
    plt.grid(True)
    plt.yticks (np.arange (0, max(voltages) + 0.1, 0.05))
    plt.xticks (np.arange (0, max(numbers) + 2, 8))
    plt.xlabel("numbers")
    plt.ylabel("voltages")
    plt.show()