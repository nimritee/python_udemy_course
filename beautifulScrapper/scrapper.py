import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.timeanddate.com/weather/germany"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5libcl

tables = soup.find_all('table')
table = soup.find('table', class_='zebra fw tb-wt zebra va-m')

# Defining of the dataframe
df = pd.DataFrame(columns=['Location', 'Temperature', 'Recorded Time', 'Description'])

# Collecting Ddata
for row in table.tbody.find_all('tr'):    
    columns = row.find_all('td')     # Find all data for each column

    if(columns != []):
        location = columns[0].text.strip()
        recorded_time = columns[1].text.strip()
        description = str(columns[2].img['alt'])
        temperature = columns[3].text.strip()

        df = df.append({'Location': location,  'Temperature': temperature, 'Recorded Time': recorded_time, 'Description':description}, ignore_index=True)
        location=None
        temperature=None
        recorded_time=None
        description=None

        location = columns[4].text.strip()
        recorded_time = columns[5].text.strip()
        description = str(columns[6].img['alt'])
        temperature = columns[7].text.strip()
        

        df = df.append({'Location': location,  'Temperature': temperature, 'Recorded Time': recorded_time, 'Description':description}, ignore_index=True)
        location=None
        temperature=None
        recorded_time=None
        description=None


        location = columns[8].text.strip()
        recorded_time = columns[9].text.strip()
        # description = str(columns[10].img['alt'])
        temperature = columns[11].text.strip()
        

        df = df.append({'Location': location,  'Temperature': temperature, 'Recorded Time': recorded_time, 'Description':description}, ignore_index=True)
        location=None
        temperature=None
        recorded_time=None
        description= None

print(df)
df.to_csv('weather.csv')