# Project 3 - Predicting subreddit posts

## Executive Summary

### Problem Statement

There was an unfortunate power outage on some of the servers which stored some of the posts of the subreddits:r/travel and r/backpacking. This caused the reddit posts to be stored incorrectly within the servers.

As an employee of Reddit, my boss has tasked me with correctly classifying these posts by training a classifier model to correctly identify the subreddit in which they belong to.

We will be training 2 models (Naive Bayes and Random Forests) based on about 2000 reddit posts webscraped from the subreddits online (1000 posts from each subreddit).  

### process

- Data collection via Pushshift API
- Data cleaning
- Preprocessing data to conduct some exploratory data analysis
- Modeling with Multinomial Naive Bayes and Random Forest


### Data Collection

Pushshift API was used for web scrapping of the subreddit submission posts. Each web scrapping was capped at 100 posts and we created a function to account for duplicated posts and dropping them if there were any. In total, 998 posts from backpacking subreddit were collected and 1051 posts from travel subreddit were collected. We then saved both groups of data into their csv files respectively.

### Data Cleaning

After reading in the data into the notebook, the first step was to check for missing values. I realized that there were a few rows with null values in it and proceeded to drop them. We also removed submission posts which had metadata like '[removed]' since they would not be relevant in our task. We also used the author columns to check for any moderator bot messages which there were none.

Once done, we proceeded to combine both csv files into a single dataframe. The following were conducted:

- removing other metadata
- lowercasing all texts
- removing whitespaces at ends of the texts
- removing hyperlinks
- removing numbers

We then used the RegexpTokenizer to tokenize the words and lemmatize them to bring all the words into their root form. This would like to consolidate the words when counting their frequency during the exploratory data analysis phase. We also added additional stopwords and included the title of the subreddits: backpacking and travel to prevent our models from predicting posts too easily.


## Exploratory Data Analysis (EDA)

We did a preliminary EDA to dive deeper into our text data. For each subreddit, we respectively looked at:

- longest and shortest posts by character letters
   - Overall, backpacking had the longest post (37,978 characters)
   - Overall, backpacking had the shortest post (7 characters)
- longest and shortest posts by word count
   - Overall, backpacking had the longest post (7,493 words)
- distribution of post length and word count (1 word)
- Unique users and average post per user
   - Backpacking: 832 unique users, 1.19 average post per user
   - Travel: 969 unique users, 1.08 average post per user
- 10 most frequent words based on normal text and lemmatized texts (using CountVectorizer and TF-IDF Vectorizer)
   - Backpacking subreddit:
     - CountVectorizer:
       - normal text: trip, day, looking, get, time, trail, go, know, anyone, first
       - lemmatized text: day, trip, time, trail, looking, get, go, know, anyone, first
     - TF-IDF Vectorizer:
       - normal text: trip, looking, anyone, get, know, go ,day, time, trail, first
       - lemmatized text: trip, day, looking, anyone, get, know, time, go, trail, first

   - Travel subreddit:
     - CountVectorizer:
       - normal text: day, trip, go, time, days, get, know, us, looking, flight
       - lemmatized text: day, trip, time, go, flight, get, know, country, place, city
     - TF-IDF Vectorizer:
       - normal text: trip, go, time, know, looking, get, us, days, day, flight
       - lemmatized text: day, trip, time, go, flight, get, know, country, place, city

- Most common bigrams and trigrams


### Preprocessing and Modeling / Evaluation

CountVectorizer and TfidfVectorizer from scikit-learn were used to convert the text data to numeric features. TfidfVectorizer achieved better accuracy scores for both our Naive Bayes and Random Forest models. Both models were also tuned with Gridsearch. Naive Bayes with TfidfVectorizer and Gridsearch performed the best at 0.8235.


### Takeaways and Recommendations

1. For the 2 subreddits: Naïve Bayes marginally performs better than Random Forest. 
2. Surprisingly, the concern for the naïve assumption that all features are independent has minimal impact to the model’s capability to classify the reddit posts accurately
3. Naive Bayes is easy to train and understand the results while Random Forest takes time to train and consumes more time to predict
