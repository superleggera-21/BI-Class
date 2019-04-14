# import numpy as np
# import scipy as sc
import pandas as pd
# import matplotlib as mpl
# import seaborn as sns

import os
print(os.getcwd())
df = pd.read_csv('Salaries.csv')

# print(df.head(30))
# print(df['salary'].dtype)
# print(df.dtypes)

# print(len(df))
# print(df.shape)
# print(df.size)
# print(df.columns)
# print(df.dtypes)

# print(df.head(50).mean())

# print(df.salary.describe())
# print(df.salary.count())
# print(df.salary.mean())

# df_rank = df.groupby('rank')
# print(df_rank.mean())
# print(df.groupby(('rank'), sort=False)[['salary']].mean())

df_sub = df[ df['salary'] > 120000 ]
df_f = df[ df['sex'] == 'Female']

#select column salary:
df['salary']

#select multiple columns(double bracket has to be used!):
df[['salary','rank']]

#select via number
print(df[0:10])
print(df_sub.loc[10:20,['rank','sex','salary']])
