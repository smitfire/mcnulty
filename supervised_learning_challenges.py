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
  cat_counts    = df.stack().value_counts()
  num_yes_votes = cat_counts[0]
  num_no_votes  = cat_counts[1]
  prob_yes      = "{0:.2f}".format(num_yes_votes/float(num_yes_votes+num_no_votes))
  df            = df.replace(['?'], [prob_yes])
  return df



# CHALLENG TWO
data            = challenge_one()
train, test     = train_test_split(data, train_size = 0.8)

print train.head(), test.head()
