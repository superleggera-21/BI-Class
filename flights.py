import pandas as pd
import numpy as np

flights = pd.read_csv('flights.csv')

# find all of the rows that have Null in any entry of the columns
print(flights[flights.isnull().any(axis=1)].head())
# Print the min, mean and max for delays for arr and dep
flights = flights.dropna()
print(flights[['dep_delay','arr_delay']].agg(['min','mean','max']))
