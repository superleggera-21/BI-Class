# Quiz 2 Instructions: Type the code under each question.
# Make sure the complete file will run at one go and not a question at a time
# (use different variables)
# After you are finished with your program, at the end, remove all unnecessary print statements.
# Type your name here:
# Jingyu He
## Part 1: Native Python (30 points)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Question 1: (10 points)
# The area of a rectangle is the rectangle’s length times its width.
# Write a program that asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater area,
# or if the areas are the same.
def triangle():
    l1 = input('Please enter the length of the first triangle')
    w1 = input('Please enter the width of the first triangle')
    l2 = input('Please enter the length of the second triangle')
    w2 = input('Please enter the width of the second triangle')
    a1 = float(l1) * float(w1) * 0.5
    a2 = float(l2) * float(w2) * 0.5
    if a1 > a2:
        print('The first triangle is bigger')
    elif a2 > a1:
        print('The second triangle is bigger')
    else:
        print('They are equally sized.')

triangle()
# Question 2: (10 points)
# Write a program that asks the user for a number.  Check to see if the number is positive, negative or zero.
# Display the appropriate message: e.g. 'Positive number', 'Negative number', 'Zero'.  Use Elif statements
def checker(x):
    if x > 0:
        print('Positive number')
    elif x < 0:
        print('Negative number')
    else:
        print('Zero')

checker()
# Question 3: (10 points)
# Modify the previous question so that until the user enters a positive number, it keeps asking the user for a number
# and displaying the appropriate message(s).

def checker2(x):
    checker(x)
    while x > 0:
        x = input("Please enter a new number")
        if x > 0:
            print('Positive number')
        elif x < 0:
            print('Negative number')
        else:
            print('Zero')

checker2()
## Part 2: DATA SCIENCE (30 points)

# Read the file MIS3545_students.csv found in the blackboard quiz. (1 point)

# 1 Display the first five rows (3 points)
import os
print(os.getcwd())
df = pd.read_csv('MIS3545_Students.csv')
print(df.head(5))
# 2 How many students are in this class? (3 points)
print('There are ',str(len(df)),' students in the class.')
# 3 Summarize the student grade sheet (the complete data) (3 points)
print(df.describe())
# 4 Select the rows where Test_1 score is greater than 80 and gender is female ('F') (7 points)
df_t1hi = df[df['Test_1'] > 80]
print(df_t1hi[df_t1hi['Gender'] == 'F'])
# 5 Calculate the mean of Test_1, Test_2, Test_3 (3 points)
print('Test 1: ', str(df['Test_1'].mean()))
print('Test 2: ', str(df['Test_2'].mean()))
print('Test 3: ', str(df['Test_3'].mean()))
# 6 Students who did not complete an assignment, test or quiz should get a zero.
# Replace all the missing values with zero and display the new summary (3 points)
df.fillna(0, inplace = True)
print(df.describe())
# 7 Display a barplot where x is the 'Type', y is the 'Test_1' score and it is split by Gender (5 points) (7 points)
sns.set_style("whitegrid")
ax = sns.barplot(x='Type',y ='Test_1', hue='Gender', data=df, estimator=len)
plt.show()
# BONUS (5 points)
# Each test, assignment and quiz are equally weighted.
# Therefore, the final grade is the average of all the scores for each student.
# Who got the highest grade? [hint: create a new column for average of each row, sort it descending and print out the
# first row]

scores = df.mean(axis=1)
df['Scores'] = scores
new = df.sort_values(by=['Scores'], ascending=False)
print(new.head(5))
best = new.iloc[0:1]
print("The person below has highest score: ")
print(best)
## Part 3: Twitter (30 points)

# A professor at Babson wondered how everyone thought of the different teams from Massachusetts and which team has the
# highest positive polarity average.  Therefore modify the Twitter the following way:
import tweepy
from textblob import TextBlob



consumer_key = 'i8g7flRE838Hgn5Qq5nnXU6qW'
consumer_secret = 'cYZGXIkcrJdPY0ekJ3SoWfG1amKM97jLKIcJq1nPQ0N8r40Ldd'

access_token = '2583536299-2Gn3OZUjI26e75XzyjDrF9PHm04Dq2XGYNOkywi'
access_token_secret = 'N9c0fFHAY6I5GSNdF7mKQY6ecZg9JZLHbyuWdphcspJQU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# Look up three teams: 'Red Sox', 'Celtics', 'Bruins' (10 points)

RS_tweets = api.search('Red Sox')
C_tweets = api.search('Celtics')
B_tweets = api.search('Bruins')

# Calculate the overall average polarity for each team (10 points)
polrs = 0
countrs = 0
for tweet in RS_tweets:
    analysis = TextBlob(tweet.text)
    polrs += analysis.sentiment[0]
    countrs += 1
resrs = polrs/countrs
print('red sox: ', str(resrs))

polc = 0
countc = 0
for tweet in C_tweets:
    analysis = TextBlob(tweet.text)
    polc += analysis.sentiment[0]
    countc += 1
resc = polc/countc
print('Celtics: ', str(resc))

polb = 0
countb = 0
for tweet in B_tweets:
    analysis = TextBlob(tweet.text)
    polb += analysis.sentiment[0]
    countb += 1
resb = polb/countb
print('Bruins: ', str(resb))
# Compare the three averages and print out which team has the highest average polarity (10 points)
avgs = [resrs, resc, resb]
print("highest is: ", str(max(avgs)))
#Bonus (3 points)
#Ask the user to enter three team/topic and tell the user which team/topic has the highest average polarity

## Part 4: Create your own question (10 points)
# Write your own python question and its answer from any one of the above categories.
# Extra points will be given for creativity or a modification in Twitter.

def convertctof(c):
    f = (f-32)*(5/9)
    print('c degree in farenheit is: ', str(f))

findbmi()