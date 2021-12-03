# Bernoulli Distribution
# Parameters:
    # size : 

from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import seaborn as sb

# Plot the graph
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,15))

size = 1000
p=0.2
for i,ax in zip(range(16),ax.ravel()):
    data_bern = bernoulli.rvs(size=size,p=p)
    sb.distplot(data_bern,kde=True,ax=ax)
    ax.set(xlabel='size ={} and p ={}'.format(size,p))
    size = size + (i*100)
    p = p + 0.1
plt.show()