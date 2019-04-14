import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# For this data frame, write the code in python using Pandas and answer the following questions:

#     Get the first three rows of data
df = pd.DataFrame(index=labels, data = exam_data)

print(df.head(3))
#     Select the 'name' and 'score' columns
print(df[['name','score']])
#     Select 'name' and 'score' columns in rows 1, 3, 5, 6
print(df.loc[['a','c','e','f'],['name','score']])
#     select the rows where the number of attempts in the examination is greater than 2
print(df[df['attempts']>2])
#     count the number of rows and columns
print(df.shape)
#     select the rows where the score is missing, i.e. is NaN
print(df[df['score'].isnull()])
#     select the rows the score is between 15 and 20 (inclusive)
print(df[df['score']<20][df['score']>15])
#     select the rows where number of attempts in the examination is less than 2 and score greater than 15
print(df[(df['attempts'] < 3) & (df['score'] > 15)])
#      calculate the sum of the examination attempts by the students
print(df['attempts'].sum())
#     calculate the mean score for each different student
df.dropna()
print(df.groupby(['qualify'])[['score']].mean())