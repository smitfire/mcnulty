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

def data_to_csv(total):
    with open("data.csv", "wb") as movies:
        writer = csv.writer(movies)
        header = read_headers()
        writer.writerow(header)
        for i, row in enumerate(total):
            writer.writerow(row)

def form_data(f):
    f= open(f, "r")
    rf = f.read().replace("\n", " ").replace(".","")
    # rf = f.read().replace("\n", " ").replace(".","").replace("-9", "NaN")
    rf = rf.split("name")
    return [ item.split() for item in rf if len(item.split()) == 75]


hung = form_data("hungary.data")
ch = form_data("switz.data")
cleveland = form_data("cleveland.data")

total = hung + ch + cleveland


data_to_csv(total)
pp(total[0])
print len(total[0])

