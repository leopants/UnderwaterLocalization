import pandas as pd
import json

data = pd.read_csv("june11_10_30.log", ';')

print(data[['Latitude', 'Longitude', 'Time', 'Date',
            'Total Water Column (m)', 'Temperature (c)', 'pH', 'ODO mg/L']])
