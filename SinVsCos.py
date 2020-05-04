import numpy as np
import matplotlib.pyplot as plt


def cc():
    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, x, z)
    plt.show()


cc()
