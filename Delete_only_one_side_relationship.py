#!/usr/bin/python
import os
import MySQLdb
import mysql.connector
from collections import defaultdict
from collections import Counter
PinLiang = mysql.connector.connect(host='127.0.0.1', user='root', 
passwd='123', db='chatchat', buffered=True)
findsomething = PinLiang.cursor()
findsomething.__class__
findsomething.execute("select * from room_members order by roomid")
row=findsomething.fetchall()
a=[]
b=[]
c=[]
d=[]
print len(Counter(row))
for x in range(len(Counter(row))):
    a.append(row[x][0])
counts = dict()
for i in a:
    counts[i] = counts.get(i,0)+1
q = dict((k, v) for k, v in counts.iteritems() if v==1)
print len(q)
c=sorted(q)
print c
for x in range(len(q)):
#    print c[x]
#    findsomething.execute("select title from room where id =11")
#    findsomething.execute("select title from room where id = %s and room_type='ONE_TO_ONE'" % c[x])
#    d.append(findsomething.fetchall()) 
#print d 
   findsomething.execute("delete from room_members where roomid=%s" % c[x])
   findsomething.execute("delete from room where id=%s" % c[x])
   PinLiang.commit()
findsomething.close() 
PinLiang.close()


