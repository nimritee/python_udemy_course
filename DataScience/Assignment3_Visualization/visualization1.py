# The  first data set contains a single categorical variable describing the religion of the people in Germany.
# There are in total 18084 persons contained in the data set and twelve levels, e.g.: Una liated, Catholic
# Church, Evangelical Church or Islam

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Read the csv data
data = pd.read_csv('data1.csv')

religion_data = {}

# Store the count of people, following a particular religion
for i in data['religion'].unique().tolist():
    religion_data[i]=((data['religion']== i).sum())

# Sort the data in descending order
sorted_religion_data = dict(sorted(religion_data.items(), key=lambda x: x[1], reverse=True))

religion = list(sorted_religion_data.keys()) # List of all religion 
count = list(sorted_religion_data.values()) # Count of people for a particular region

# Plot the Graph 
fig, ax = plt.subplots(figsize=(15, 6))
plt.xscale("log") # Use logarithmic Scale
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True)) # Convert the xaxis value to Linear
plt.xlabel("Number of People")
plt.ylabel("Religion")
plt.title('Horizontal Barplot: Religion of people in Germany')
plt.barh(y=religion, width=count)
plt.show()