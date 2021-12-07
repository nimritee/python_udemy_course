# Binomial Distribution 
# Parameters: 
    # n: number of trials
    # p : probability of occurence of each trial 
    # size : The shape of the returned array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Plot the graph
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(15,15))
n=10
p = 0.1
size =1000
for i,ax in zip(range(16),ax.ravel()):
    sns.distplot(random.binomial(n=n, p=p, size=1000), hist=True, kde=False, ax=ax) 
    ax.set(xlabel='n ={} p={} size={}'.format(n,p,size),ylabel='frequency')
    n = n + 2
    p = p + 0.05
    size = size + 100
    fig.suptitle('Binomial Distribution',fontweight ="bold")
plt.show()