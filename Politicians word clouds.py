# Create word clouds with Spanish politicians' most tweeted words
# Author: Álvaro Corrales Cano
# October 2019

# Import libraries
import GetOldTweets3 as got
import os
import nltk
from nltk.corpus import stopwords 
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Set our working directory
directory = '---INSERT WORKING DIRECTORY---'
os.chdir(directory)

# Define politicians
politicians = ['sanchezcastejon', 'Albert_Rivera', 
               'Pablo_Iglesias_', 'pablocasado_', 'Santi_ABASCAL', 
               'ierrejon']

# Define some functions and criteria to be used later
def get_tweets(user, start_date, end_date):
    
    tweetCriteria = got.manager.TweetCriteria().setUsername(user)\
                                           .setSince(start_date)\
                                           .setUntil(end_date)\

    tweet = got.manager.TweetManager.getTweets(tweetCriteria)

    return tweet

stop_words_eng = set(stopwords.words('english')) 
stop_words_esp = set(stopwords.words('spanish')) 
extra_stop = ['https', 'si', 'no', 'gracias', 'hoy', 'todas', 'ahora', 'aquí',
              'allí', 'junto', 'años', 'gran', 'grande', 'toda', 'partir', 
              'hace', 'ver', 'dos', 'ser']

def filter_words(bag):
    
    filteredWords = [w for w in bag if not w in stop_words_eng] 
    filteredWords = [w for w in filteredWords if not w in stop_words_esp]
    filteredWords = [w for w in filteredWords if not w in extra_stop]    
    filteredWords = [w for w in filteredWords if w.isalpha()]     

    return filteredWords

# Produce word clouds in a loop
for politician in politicians:
    
    print(" ")
    print("Político:", politician)
    
    # Get tweets in a time frame
    tweet = get_tweets(politician, 
               start_date = "2019-07-09", end_date = "2019-10-09")
    
    # Get text bag
    textTweets = []
    textBag = []
    for i in range(len(tweet)):
        text = tweet[i].text
        textTweets.append(text.lower())
        words = nltk.word_tokenize(textTweets[i])
        filteredWords = filter_words(words)
        textBag.extend(filteredWords)

    # Word cloud
    if politician == 'sanchezcastejon':
        colors = 'Reds'
        
    elif politician == 'Albert_Rivera':
        colors = 'Oranges'
    
    elif politician == 'Pablo_Iglesias_':
        colors = 'Purples'
        
    elif politician == 'pablocasado_':
        colors = 'Blues'
    
    elif politician == 'Santi_ABASCAL':
        colors = 'Greens'
    
    elif politician == 'ierrejon':
        colors = 'Greys'
    
        
    cloud = WordCloud(max_words=50, background_color="white",
                  colormap = colors).generate(" ".join(textBag))

    plt.imshow(cloud, interpolation='bilinear')
    plt.axis("off")
    
    plt.savefig("output/cloud_" + politician + ".png", 
            format="png")
    
    plt.show()
