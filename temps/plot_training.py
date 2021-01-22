import numpy as np
import matplotlib.pyplot as plt

a = np.load('./trained_models/run_2021_01_14_00_30/fishnchips_250_5CNN_25H_4B_6MPK.npy')
x = []
for e in a:
    x.append(e[0])


values=np.cumsum(np.random.randn(1000,1))
plt.plot(x)
plt.show()

print('ploted')