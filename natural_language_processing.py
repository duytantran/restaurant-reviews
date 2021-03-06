# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t'
                      , quoting = 3) # 3 means ignoring the double quotes

# Cleaning the texts
import re
import nltk
#nltk.download('stopwords') # uncomment if the stopwords package isn't installed
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = [] # collection of texts of the same type
N = 1000 # size of dataframe
for i in range(0, N):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review 
          if not word in set(stopwords.words('english'))] # use set for faster computation
    review = ' '.join(review) # reverses the list back into a string
    corpus.append(review)
    
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray() # Could of course use dimensionality reduction for the sparse matrix too
y = dataset.iloc[:, 1].values 

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred) #73% accuracy