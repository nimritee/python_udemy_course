# The second data set includes data on the salary of people in Germany. The data is accomplished by the
# age of each person and whether he or she works in the East or West of Germany.

import pandas as pd
import matplotlib.pyplot as plt

# Read the csv data
data = pd.read_csv('data2.csv')

# Sort the values, according to the part of Germany
east_germany = data.loc[data['part.of.germany'] == 'east'].sort_values(by=['age'])
west_germany = data.loc[data['part.of.germany'] == 'west'].sort_values(by=['age'])

# Plot the Graph 
plt.plot(east_germany['age'],east_germany['salary'], marker='', color='red', linewidth=1, alpha=0.9, label='East Germany')
plt.plot(west_germany['age'],west_germany['salary'], marker='', color='green', linewidth=1, alpha=0.9, label='West Germany')

plt.title('Line Chart: Salary of people in Germany')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.show()