import numpy as np
import matplotlib.pyplot as plt

def Draw_Graph(subject):
    mandata = Extract_data_man(subject)
    womandata = Extract_data_woman(subject)

    mscores = np.array(list(mandata.keys()))
    mcounts = np.array(list(mandata.values()))
    wscores = np.array(list(womandata.keys()))
    wcounts = np.array(list(womandata.values()))

    a, b = np.histogram(mscores, weights=mcounts, bins=30, density=True)
    man_x = (b[:-1] + b[1:]) / 2  # 구간 중심 계산
    e = np.interp(np.linspace(b[0], b[-1], 300), man_x, a)

    c, d = np.histogram(wscores, weights=wcounts, bins=30, density=True)
    woman_x = (d[:-1] + d[1:]) / 2
    f = np.interp(np.linspace(d[0], d[-1], 300), woman_x, c)

    plt.figure(figsize=(10, 6))
    x_values = np.linspace(b[0], b[-1], 300)
    plt.plot(x_values, e, label="Male", color="blue")
    plt.plot(x_values, f, label="Female", color="orange")

    plt.title(f"Distribution of Scores for {subject}", fontsize=14)
    plt.xlabel("Score", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.3)

    plt.show()