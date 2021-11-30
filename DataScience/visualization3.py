# The third data set contains a single numeric variable measuring the height of !Kung San2 people.

import pandas as pd
import matplotlib.pyplot as plt

# Read the csv data
data = pd.read_csv('data3.csv')

height_data = data['height']
bins = [50,60,70,80,90,100,110,120,130,140,150,160,170,180]

# Plot the Graph
plt.hist(height_data, bins=bins, edgecolor='black')
plt.title('Histogram: Height of people in !Kung San')
plt.xlabel("Height")
plt.ylabel("Number of people")
plt.show()