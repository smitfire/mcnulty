#/usr/bin/python2.4
#
#

import psycopg2

# Try to connect

try:
    conn=psycopg2.connect("dbname='nick' user='nick' password='t00thle55' host='mcnulty'")
except:
    print "I am unable to connect to the database."

cur = conn.cursor()
try:
    cur.execute("""SELECT * from mcnulty""")
except:
    print "I can't SELECT from bar"

rows = cur.fetchall()
print "\nRows: \n"
for row in rows:
    print "   ", row[1]