# Session 16 In-class Script


# # Import Python Libraries
# import pandas as pd
#
# # Read csv file
# df = pd.read_csv('C:/Users/ssharma6/PycharmProjects/untitled/Examples/salaries.csv')
# print(df)
# # Display a few first records
# print(df.head(10))
# # Display first 10 records
#
# # Display the last 5 records
# print(df.tail())
# # Check the type of a column "salary"
# print(df['salary'].dtype)
# # List the types of all columns
# print(df.dtypes)
# # Find how many records this data frame has?
# print(df.shape)
# # How many elements are there?
# print(df.size)
# # What are the column names?
# print(df.columns)
# # What types of columns we have in this data frame?
#
# # Give the summary for the numeric columns in the dataset
# print(df.describe())
# # Calculate standard deviation for all numeric columns;
#
# # What are the mean values of the first 50 records in the dataset?
#
# print(df.head(50).mean())
# # Calculate the basic statistics for the salary column;
# print(df['salary'].describe())
# # Find how many values in the salary column (use count method);
# print(df['salary'].count())
# # Calculate the average salary;
# print(df['salary'].mean())
# #
# # dfg = df.groupby('rank')
# print(df.groupby('rank').mean())
# print(df.mean())
# # Select only those rows that have salary > 100k
# print(df[df['salary'] > 100000])
# # Select only those rows that have rank = Professor and are female
# print(df[(df['rank'] == 'Prof') & (df['sex'] == 'Female')])
# # Select 5 records appearing in the dataframe from position 10 onwards
# print(df[10:15])
# # Select 5 records appearing in the dataframe from position 10 onwards only with rank and salary data
# print(df.loc[10:14,['rank','salary']])
# # Select 7th to 10th rows with last two columns
#
# # Sort all the records by salary in descending order
#
# # Read a dataset with missing values
# flights = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/flights.csv")
# print(flights.head())
# # Select the rows that have at least one missing value
# print(flights[flights.isnull().any(axis=1)].head(100))
# print(flights[flights.isnull().any(axis=1)])

import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data)
print(df)