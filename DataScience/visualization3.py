# The third data set contains a single numeric variable measuring the height of !Kung San2 people.

import pandas as pd
import matplotlib.pyplot as plt

# Read the csv data
data = pd.read_csv('data3.csv')

# Create range of height, for plotting the data
data['bar_bins'] = pd.cut(data.height,bins=[50,75,100,125,150,175,200],labels=['50-75','76-100','101-125','126-150','151-175','176-200'])
bar_data= data['bar_bins'].value_counts().reset_index()

# Plot the Graph
plt.bar(bar_data['index'], bar_data['bar_bins'])
plt.ylabel('Count')
plt.xlabel('Height')
plt.title('Barplot: Height of people in !Kung San')
plt.show()