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
# train, test     = train_test_split(data, train_size = 0.8)

# print train.head(), test.head()

print data[1].mode() + 4


# CHALLENGE THREE

# me_range = list(xrange(1,30))

# x_train  = train.iloc[:,1:]
# y_train  = train.iloc[:,0]

# x_test   = test.iloc[:,1:]
# y_test   = test.iloc[:,0]


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

# model   = LogisticRegression()
# model.fit(x_train, y_train)
# y_pred  = model.predict(x_test)
# a_score = accuracy_score(y_test, y_pred)


# print "LOGISTIC REGRESSION TEST SCORE:"
# print a_score



# CHALLENGE FIVE


# df.head()
# ndf = df[[0, 1]]
# ndf.head()
# ndf2 = ndf.groupby([0]).count()
# ndf2.head()
# ndf2.plot(kind="bar")

# num_dems, num_reps = df.stack().value_counts()[2], df.stack().value_counts()[3]

# def dem_list(X):
#   return ("democrat "*len(X)).strip().split()

# def rep_list(X):
#   return ("republican "*len(X)).strip().split()

# model   = LogisticRegression()
# model.fit(x_train, y_train)
# y_pred  = dem_list(list(xrange(1,88)))
# a_score = accuracy_score(y_test, y_pred)
# y_pred  = rep_list(list(xrange(1,88)))
# b_score = accuracy_score(y_test, y_pred)

#  Dems, Reps Score for Challenge 5
# print a_score, b_score
