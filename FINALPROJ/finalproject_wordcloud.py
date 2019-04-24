import pandas as pd
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import csv

# dfus = pd.read_csv('USvideos_new.csv', engine='python')

# dftus = dfus.transpose()

# dffus = dftus.iloc[7]

# wordcloud = WordCloud(
#     width = 3000,
#     height = 2000,
#     background_color = 'white',
#     stopwords = STOPWORDS).generate(str(dffus))

# fig = plt.figure(
#     figsize = (40, 30),
#     facecolor = 'k',
#     edgecolor = 'k')

# plt.imshow(wordcloud, interpolation = 'bilinear')
# plt.axis('off')
# plt.tight_layout(pad=0)
# plt.show()

# dfuk = pd.read_csv('UKvideos_new.csv', engine='python')

# dftuk = dfuk.transpose()

# dffuk = dftuk.iloc[7]

# wordcloud = WordCloud(
#     width = 3000,
#     height = 2000,
#     background_color = 'white',
#     stopwords = STOPWORDS).generate(str(dffuk))

# fig = plt.figure(
#     figsize = (40, 30),
#     facecolor = 'k',
#     edgecolor = 'k')

# plt.imshow(wordcloud, interpolation = 'bilinear')
# plt.axis('off')
# plt.tight_layout(pad=0)
# plt.show()


dfca = pd.read_csv('CAvideos_new.csv', engine='python')

dftca = dfca.transpose()

dffca = dftca.iloc[9]

wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    background_color = 'white',
    stopwords = STOPWORDS).generate(str(dffca))

fig = plt.figure(
    figsize = (40, 30),
    facecolor = 'k',
    edgecolor = 'k')

plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()