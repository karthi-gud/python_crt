import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 4, 2, 1])
y = np.array([6, 9, 10, 15, 21])

# Corrected: use 'color' instead of 'ycolour'
plt.scatter(x, y, color='g') # 'g' stands for green

plt.show()