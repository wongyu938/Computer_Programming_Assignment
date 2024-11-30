import numpy as np
import matplotlib.pyplot as plt

def Draw_Graph(subject):
    man_data = Extract_data_man(subject)
    woman_data = Extract_data_woman(subject)

    man_scores = np.array(list(man_data.keys()))
    man_counts = np.array(list(man_data.values()))
    woman_scores = np.array(list(woman_data.keys()))
    woman_counts = np.array(list(woman_data.values()))

    man_hist, man_bins = np.histogram(man_scores, weights=man_counts, bins=30, density=True)
    man_x = (man_bins[:-1] + man_bins[1:]) / 2 
    man_smooth = np.interp(np.linspace(man_bins[0], man_bins[-1], 300), man_x, man_hist)

    woman_hist, woman_bins = np.histogram(woman_scores, weights=woman_counts, bins=30, density=True)
    woman_x = (woman_bins[:-1] + woman_bins[1:]) / 2
    woman_smooth = np.interp(np.linspace(woman_bins[0], woman_bins[-1], 300), woman_x, woman_hist)

    plt.figure(figsize=(10, 6))
    x_values = np.linspace(man_bins[0], man_bins[-1], 300)
    plt.plot(x_values, man_smooth, label="Male", color="blue")
    plt.plot(x_values, woman_smooth, label="Female", color="orange")

    plt.title(f"Distribution of Scores for {subject}", fontsize=14)
    plt.xlabel("Score", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.3)

    plt.show()