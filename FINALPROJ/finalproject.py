import pandas as pd
import numpy as np
import os
# df = pd.read_csv('USvideos_new.csv', engine='python')
# print(df.head(5))

# from textblob import TextBlob
# pola = []
# polas = []
# subj = []
# subjs = []
# for index, row in df.iterrows():
#     analysis = TextBlob(row['title'])
#     pola.append(analysis.sentiment[0])
#     subj.append(analysis.sentiment[1])
#     if type(row['description']) == type('str'):
#         analysis2 = TextBlob(row['description'])
#         polas.append(analysis2.sentiment[0])
#         subjs.append(analysis2.sentiment[1])
#     else:
#         polas.append(0)
#         subjs.append(0)


# df['polarity'] = pola
# df['subjectivity'] = subj
# df['polarity_description'] = polas
# df['subjectivity_description'] = subjs
# print(df.head(5))
# df.to_csv('out.csv')

# df = pd.read_csv('UKvideos_new.csv', engine='python')
# print(df.head(5))

# from textblob import TextBlob
# pola = []
# polas = []
# subj = []
# subjs = []
# for index, row in df.iterrows():
#     analysis = TextBlob(row['title'])
#     pola.append(analysis.sentiment[0])
#     subj.append(analysis.sentiment[1])
#     if type(row['description']) == type('str'):
#         analysis2 = TextBlob(row['description'])
#         polas.append(analysis2.sentiment[0])
#         subjs.append(analysis2.sentiment[1])
#     else:
#         polas.append(0)
#         subjs.append(0)


# df['polarity'] = pola
# df['subjectivity'] = subj
# df['polarity_description'] = polas
# df['subjectivity_description'] = subjs
# print(df.head(5))
# df.to_csv('outuk.csv')

df = pd.read_csv('CAvideos_new.csv', engine='python')
print(df.head(5))

from textblob import TextBlob
pola = []
polas = []
subj = []
subjs = []
for index, row in df.iterrows():
    analysis = TextBlob(row['title'])
    pola.append(analysis.sentiment[0])
    subj.append(analysis.sentiment[1])
    if type(row['description']) == type('str'):
        analysis2 = TextBlob(row['description'])
        polas.append(analysis2.sentiment[0])
        subjs.append(analysis2.sentiment[1])
    else:
        polas.append(0)
        subjs.append(0)


df['polarity'] = pola
df['subjectivity'] = subj
df['polarity_description'] = polas
df['subjectivity_description'] = subjs
print(df.head(5))
df.to_csv('outca.csv')