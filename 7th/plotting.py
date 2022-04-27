import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_data(path_to_data: str):
    with open(path_to_data, "r") as file_:
        data_str = file_.read().split()
        data = np.array(list(map(float, data_str)))

    return data


def read_stats(path_to_stat: str):
    df = pd.read_csv(path_to_stat)

    return df


def count_times(data: np.ndarray, freq: float, total_time: float):
    charging_time = data.argmax() * freq
    discharging_time = total_time - charging_time

    return charging_time, discharging_time
    

def plot_data(path_to_data: str, path_to_stat: str, figsize=(18, 12), markerevery=5, markerstyle="o", color="red",
                save_graph=False, save_name=None):

    data = read_data(path_to_data)
    stat = read_stats(path_to_stat)
    total_time = stat["Total time"][0]
    freqs      = stat["Frequency"][0]

    Y_values = data
    X_values = np.arange (start=freqs, stop=total_time, step=freqs)
    charg_time, discharg_time = count_times (data, freqs, total_time)
    fig, ax = plt.subplots(figsize=figsize, dpi=100)
    ax.minorticks_on()
    plt.plot(X_values, Y_values, marker=markerstyle, markevery=markerevery, label="V(t)", color="red")

    plt.text(0.82*X_values.max(), 0.8*Y_values.max(), f"Total time is: {total_time:.2f} secs\n"
                    f"Charging time is: {charg_time:.2f}\n"
                    f"Dischargind time is: {discharg_time:.2f}\n",
             bbox={"facecolor": "white",
                   "boxstyle": "round",
                   },
            )
        
    plt.xlabel("Time, seconds")
    plt.ylabel("Voltage, Volts")
    plt.title("Process of capacitor's charging in RC-circut")
    plt.grid(which="major", linestyle="-", linewidth=1)
    plt.grid(which="minor", linestyle="--", linewidth=0.4)
    plt.legend()

    if save_graph and save_name is not None:
        plt.savefig(save_name)

    plt.show()


if __name__ == "__main__":
    PATH_TO_DATA = "./data/data.txt"
    PATH_TO_STAT = "./data/settings.csv"

    plot_data(PATH_TO_DATA, PATH_TO_STAT, save_graph=True, save_name="./data/RC_graph.svg")
