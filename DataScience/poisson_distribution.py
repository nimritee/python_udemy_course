# Poisson Distribution 
# Parameters:
    # lam : rate or known number of occurences
    # size - The shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Plot the graph
fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(20,25))
size = 1000
lam=2
for i,ax in zip(range(16),ax.ravel()):
    sns.distplot(random.poisson(lam=lam, size=size), kde=False, ax=ax)
    ax.set(xlabel='lam ={} and size ={}'.format(i,size))
    size = size + (i*100)
    lam = lam + 2
plt.show()