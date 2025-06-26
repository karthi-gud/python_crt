import matplotlib.pyplot as plt
import numpy as np

# Corrected: Use np.array()
ypoints = np.array([3, 8, 1, 10])

# Plotting with circle markers, a dotted red line, and large marker size
plt.plot(ypoints, 'o:r', ms=25)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints,'o:r',ms=25,mec='g')
plt.show()