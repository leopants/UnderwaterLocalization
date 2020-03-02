import pandas as pd

data = pd.read_csv("june11_10_30.log", ';')

selected_data = data[['Latitude', 'Longitude', 'Time', 'Date',
                      'Total Water Column (m)', 'Temperature (c)', 'pH', 'ODO mg/L']]

print(selected_data)
