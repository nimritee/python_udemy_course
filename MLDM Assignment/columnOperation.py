import pandas as pd
import math

df = pd.read_csv('data.csv')

for i in df['y_original']:
    sqrt= math.sqrt(i)

df['sqrt(y)'] = sqrt
df.to_csv('data.csv')