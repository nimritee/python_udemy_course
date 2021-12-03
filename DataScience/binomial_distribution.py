# Binomial Distribution 
# Parameters: 
    # n: number of trials
    # p : probability of occurence of each trial 
    # size : The shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Plot the graph
fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(5,5))
n=10
p = 0.1
size =1000
for i,ax in zip(range(16),ax.ravel()):
    sns.distplot(random.binomial(n=n, p=p, size=1000), hist=True, kde=False, ax=ax) 
    ax.set(xlabel='n ={} size={}'.format(n,size))
    n = n + 2
    p = p + 0.05
    size = size + 100
plt.show()