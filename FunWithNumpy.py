"""
    === Scott Willard
"""
import numpy as np
import matplotlib.pyplot as plt

radius = np.arange(0, 5, 0.01)
circumference = 2 * np.pi*radius

ax =plt.subplot(111, projection = 'polar')
ax.plot(circumference, radius)
ax.set_rticks([0, 1, 2, 3, 4, 5])
ax.set_rlabel_position(0)
ax.grid(True)
plt.show()
