# Normal Distribution 
# Parameters: Mean and Standard Deviation 

import numpy as np 
import matplotlib.pyplot as plt

# Plot the graph
fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(20,25)) 
ax = ax.ravel()
scale = 40

for i in range(16):
    ax[i].hist(np.random.normal(loc=i, scale =scale, size=(100000)),bins=85)
    ax[i].set_xlabel('mean ={} and sd ={}'.format(i,scale))
    ax[i].set_ylabel('Frequency')
    scale = scale + 10
plt.show()