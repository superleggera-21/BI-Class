import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read file
df = pd.read_csv('Sale_Prices_City.csv')
# select Chicago as the city
df = df[0:2]
# pop out all data that can skew the average
df1 = df.iloc[:,4:]
# return average
print('The average real estate price from 2008 to 2019 of Los Angeles (0) and Chicago (1) is listed below: ')
print(df.mean(axis=1))
# Transpose the table
df2 = df1.transpose()
# Make the plot
df2.iloc[:,0:2].plot()
print('The plot is the price trend from 2008 to 2019 (by month) of Los Angeles and Chicago: ')
plt.show()
