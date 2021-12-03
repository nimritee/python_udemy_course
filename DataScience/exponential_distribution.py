# Exponential Distribution 
# Parameters
    # scale: inverse rate of (lam) deafult 1.0
    # size: the shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Plot the graph
fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(20,25))
size = 1000
for i,ax in zip(range(16),ax.ravel()):
    sns.distplot(random.exponential(scale=i,size=1000), hist=False, ax=ax) 
    ax.set(xlabel='scale ={} and size ={}'.format(i,size))
    size = size + (i*100)
plt.show()