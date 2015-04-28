import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint as pp
import csv
import datetime
from dateutil.parser import parse
from pandas.tools.plotting import scatter_matrix
from patsy import dmatrices
import statsmodels.formula.api as smf
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
import statsmodels.api as sm
import matplotlib as mpl
from numpy.random import randn
from scipy import stats
from pprint import pprint as pp
import urllib2

congressrl = "https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data"

def get_data(url):
  newrl = urllib2.urlopen(url)
  return pd.read_csv(newrl, header=-1)

def challenge_one():
  df            = get_data(congressrl)
  df            = df.replace(['y'], [1])
  df            = df.replace(['n'], [0])
  df = df.replace("?", np.nan)

  for num in list(xrange(1,17)):
      df[num] = df[num].replace(np.nan, df[num].mean())

  return df



# CHALLENGE TWO
data            = challenge_one()
train, test     = train_test_split(data, train_size = 0.8)

# print train.head(), test.head()



# CHALLENGE THREE

me_range = list(xrange(1,30))

x_train  = train.iloc[:,1:]
y_train  = train.iloc[:,0]

x_test   = test.iloc[:,1:]
y_test   = test.iloc[:,0]


# scores = []
# for num in me_range:
#   model   = KNeighborsClassifier(n_neighbors=num)
#   model.fit(x_train, y_train)
#   y_pred  = model.predict(x_test)
#   a_score = accuracy_score(y_test, y_pred)
#   scores.append((num, a_score))

# print scores
# print "K VALUE WITH HIGHEST ACCURACY:"
# scores.sort(key=lambda x: x[1])
# print scores[-1][0]
# print "Sorted scores list (k value, accuracy score)"
# print scores


# CHALLENGE FOUR

# scores = []

model   = LogisticRegression()
model.fit(x_train, y_train)
y_pred  = model.predict(x_test)
a_score = accuracy_score(y_test, y_pred)


# print "LOGISTIC REGRESSION TEST SCORE:"
# print a_score



# CHALLENGE FIVE

num_dems, num_reps = data.stack().value_counts()[2], data.stack().value_counts()[3]
print num_dems, num_reps




