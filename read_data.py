import csv, urllib2
from pprint import pprint as pp
import codecs
import numpy as np

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/new.data"

hungary="https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/hungarian.data"

def read_headers():
    with open("headers.txt", "r") as headers:
        return [ header.strip() for header in headers ]

def read_data(f):
    with open(f, "r") as f:
        reader = csv.reader(x.replace('\0', '') for x in f)
        # reader.replace("\x00",'')
        res = [ item.split() for sublist in reader for item in sublist]
        return res

def format_rows(f):
    # res = read_data(f)
    res = f.read()
    res_total = []
    for i, row in enumerate(res):
        # res2.append(row)
        res2=[]
        if i == 50:
            break
        if not row[-1] == "name":
            print row
            res2 = res2+row
        else:
            # res_total.append([ item for sublist in res[(i+1)-10:i+1] for item in sublist ])
            res_total.append(res2)
            # res_total.append()
            # res2=[]
    return res_total

def data_to_csv(total, filename):
    with open(filename, "wb") as movies:
        writer = csv.writer(movies)
        # header = read_headers()
        header = ['location', 'id','ccf','age','sex','painloc','painexer','relrest', 'pncaden','cp', 'trestbps', 'htn', 'chol','smoke', 'cigs', 'years', 'fbs', 'dm', 'famhist','restecg','ekgmo', 'ekgday', 'ekgyr', 'dig', 'prop', 'nitr', 'pro', 'diuretic','proto','thaldur','thaltime','met', 'thalach','thalrest','tpeakbps','tpeakbpd','dummy','trestbpd','exang','xhypo','oldpeak','slope','rldv5','rldv5e','ca','restckm','exerckm','restef','restwm','exeref','exerwm','thal','thalsev','thalpul','earlobe','cmo','cday','cyr','num','lmt','ladprox','laddist','diag','cxmain','ramus','om1','om2','rcaprox','rcadist','lvx1','lvx2','lvx3','lvx4','lvf','cathef','junk']
        writer.writerow(header)
        for i, row in enumerate(total):
            writer.writerow(row)

def form_data(f, location):
    f= open(f, "r")
    rf = f.read().replace("\n", " ")
    # rf = f.read().replace("\n", " ").replace(".","").replace("-9", "NaN")
    rf = rf.split(" name")
    return [ [location] + item.split() for item in rf if len(item.split()) == 75]


hung      = form_data("hung.data", "hungary")
ch        = form_data("ch.data", "switzerland")
longbeach = form_data("longbeach.data", "longbeach")
cleveland = form_data("cleve.data", "cleveland")

total = hung + ch + longbeach + cleveland


data_to_csv(total, "total2.csv")
data_to_csv(cleveland, "cleve.csv")
data_to_csv(ch, "ch.csv")
data_to_csv(hung, "hung.csv")
data_to_csv(longbeach, "longbeach.csv")

# pp(total[0])

