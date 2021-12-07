# Exponential Distribution 
# Parameters
    # scale: inverse rate of (lam) deafult 1.0
    # size: the shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Plot the graph
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(15,15))
size = 1000
for i,ax in zip(range(4),ax.ravel()):
    sns.distplot(random.exponential(scale=i+1,size=1000), ax=ax)
    ax.set(xlabel='scale ={} and size ={}'.format(i+1,size))
    size = size + (i*100)
    fig.suptitle('Exponential Distribution',fontweight ="bold")
plt.show()