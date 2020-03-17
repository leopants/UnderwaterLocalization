import pandas as pd
import numpy as np
from scipy import stats

# Read the selected file and create a pandas DataFrame
data = pd.read_csv("june11_10_30.log", ';')

# Select the necessary tags from the entire data set as a seperate DataFrame
selected_data = data[['Latitude', 'Longitude', 'Time', 'Date',
                      'Total Water Column (m)', 'Temperature (c)', 'pH', 'ODO mg/L']]

# Z-Score cannot be used with strings so remove string from the possible tags
outlier_possible = selected_data[['Latitude', 'Longitude', 'Total Water Column (m)',
                                  'Temperature (c)', 'pH', 'ODO mg/L']]

abs_z = np.abs(stats.zscore(outlier_possible))
filter_z = (abs_z < 3).all(axis=1)
print(filter_z)
outlier_possible = outlier_possible[filter_z]

print(outlier_possible)
