# Restaurant Reviews with Machine Learning
Given a dataset containing 1000 restaurant reviews, we use Natural Language Processing to seperate good and bad reviews. After creating the Bag of Words model, we classify the model with Naive Bayes.  
Coded in both Python and R.

Python NOTES:
* Use .tsv files instead of .csv for less complexity
* This code can be used in other languages than English, but beware of specific NLP classes respectively.
* Deleted 'NOT' as we assume (and truly hope) on average, that the number of misconception numbers casued by this are less in total  
* In the Python script, you can use "TD_IDF" instead of "CountVectorizer" by setting the input parameter 'normalize = None'
* Can use other classification methods such as CART, C5.0 or Maximum Entropy, but Naive Bayes gives the best accuracy.

R NOTES:
* We remove punctuation, since cross-validation has proven a better performance. It is usually a trade-off between dimensionality and information.
* Another technique than confusion matrix and CAP to test the NLP model, is the k-Fold Cross Validation. 



