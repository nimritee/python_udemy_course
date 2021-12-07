# Normal Distribution 
# Parameters: Mean and Standard Deviation 

import numpy as np 
import matplotlib.pyplot as plt

# Plot the graph
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(15,15)) 
ax = ax.ravel()
scale = 40

for i in range(4):
    ax[i].hist(np.random.normal(loc=i, scale =scale, size=(100000)),bins=85)
    ax[i].set_xlabel('mean ={} and sd ={}'.format(i,scale))
    ax[i].set_ylabel('Frequency')
    scale = scale + 10
    fig.suptitle('Normal Distribution',fontweight ="bold")
plt.show()