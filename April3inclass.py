import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read file
df = pd.read_csv('City_Of_Somerville.csv')

# display the head
print(df.head())

# list the columns
print(df.columns)

# display the number of rows and columns
print(df.shape)

# Summarize the data
print(df.describe())

# Show the mean Total Gross Salary per each Dept
df_department = df.groupby('Dept Name')
print(df_department[['Total Gross']].mean())

# show the mean Total Gross for each title within each dept
print(df.groupby(['Dept Name','Title'])[['Total Gross']].mean())

# Graph a histogram of the total gross (use distplot)
sns.distplot(df['Total Gross'])
plt.show()

# Graph a histogram of the Total Gross for each Dept (refer to ln66 in data science with answers)
df.groupby(['Dept Name'])['Total Gross'].mean().plot(kind='bar')
plt.show()

# Drop all the missing values and summarize the data
newOT = df[['OT']].fillna(df[['OT']].mean())
print(newOT.describe())