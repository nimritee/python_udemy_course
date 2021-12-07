# Bernoulli Distribution
# The bernoulli distribution is a discrete distribution that is used when a random experiment is performed and only two results are obtained,
# such as good-bad, positive-negative, success-failure.

from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import seaborn as sb

x=[0,1]
p=0.7

fig, (ax1, ax2) = plt.subplots(2)
ax1.bar(x,bernoulli.pmf(x,p),width=0.1,color=['r','b'])
ax1.set_title('Probability Mass Function for Bernoulli Distribution')

ax2.bar(x,bernoulli.cdf(x,p),width=0.1,color=['r','b'])
ax2.set_title('Cumulative Density  Function for Bernoulli Distribution')

fig.text(0.5, 0.04, 'Data Points', ha='center', va='center')
fig.text(0.06, 0.5, 'Probability', ha='center', va='center', rotation='vertical')
plt.show()