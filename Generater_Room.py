#!/usr/bin/python
import os
import MySQLdb
import mysql.connector
import time
import datetime
from collections import defaultdict
from collections import Counter
PinLiang = mysql.connector.connect(host='127.0.0.1', user='root', 
passwd='123', db='chatchat', buffered=True)
findsomething = PinLiang.cursor()
findsomething.__class__
#findsomething.execute("select id from room where room_type='ONE_TO_ONE' order by id")
findsomething.execute("select id from room order by id")    ###Delete have Room but no any room member. 
row=findsomething.fetchall()
a=[]
b=[]
c=[]
d=[]
for x in range(len(Counter(row))):
    findsomething.execute("select * from room_members where roomid=%s" % row[x][0])
    JJ=findsomething.fetchall()
    if JJ==[]:
      findsomething.execute("delete from room where id=%s" % row[x][0])
      PinLiang.commit()

findsomething.execute("select * from member_relation_ship order by friendid");
MR=findsomething.fetchall()                                ###MR All member relationship

findsomething.execute("select id from room where room_type='ONE_TO_ONE' order by id")
J1=findsomething.fetchall()
for x in range(len(J1)):
    findsomething.execute("select * from room_members where roomid=%s" % J1[x][0])
    a.append(findsomething.fetchall())

for x in range(len(a)):
    b.append((a[x][0][1],a[x][1][1]))

for x in range(len(MR)):
    Y=0
    f1=MR[x][0]
    f2=MR[x][1]
    for p in range(len(b)):
        if ((f1==b[p][0] and f2==b[p][1]) or (f1==b[p][1] and f2==b[p][0])):
           c.append((f1,f2))
           Y=1
    if Y==0:
       d.append((f1,f2))

print len(MR)        
print len(b) #Now have Room and Room member, include no member relationship.
print len(c) #Now have Room and Room member, all member have relationship.
#print len(d) #Have relationship but not have Room and Room member.
#print d[0]

def finduserid(par):
    findsomething.execute("select userid from member where id=%s" % par)
    J4=findsomething.fetchall()
    return J4[0][0]

try:				### Get Have Relation Ship but no Room and Romm member.
    for x in range(len(d)):
        N1=d[x][0]
        N2=d[x][1]
        if ((N2,N1) in d):
           d.remove((N2,N1))
except IndexError:
    print "OK"

#print d
#print len(d)

for x in range(len(d)):
    N1=d[x][0]
    N2=d[x][1]
    title=finduserid(N1)+'&&&'+finduserid(N2)
    findsomething.execute("select id from room")
    J3=findsomething.fetchall()
    g=len(J3)
    k=J3[g-1][0]
    ts=time.time()
    st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    findsomething.execute("INSERT INTO room (id, create_date_time, room_type, title, version) VALUES ('%d','%s','%s','%s','%d')" % (k+1, st , "ONE_TO_ONE", title, 1))
    findsomething.execute("INSERT INTO room_members (roomid, memberid) VALUES ('%s','%s')" % (k+1, N1))
    findsomething.execute("INSERT INTO room_members (roomid, memberid) VALUES ('%s','%s')" % (k+1, N2))
    PinLiang.commit()
print "Finish"
'''
for x in range(len(d)):
    N1=d[x][0]
    N2=d[x][1]
    Y=0
    findsomething.execute("select id from room where room_type='ONE_TO_ONE'")
    J1=findsomething.fetchall()
    for x in range(len(J1)):
        findsomething.execute("select * from room_members where roomid=%s" % J1[x][0])
        a.append(findsomething.fetchall())

    for x in range(len(a)):
        b.append((a[x][0][1],a[x][1][1]))

    for p in range(len(b)):
        if ((N1==b[p][0] and N2==b[p][1]) or (N1==b[p][1] and N2==b[p][0])):
	   Y=1
           #print "do nothing"
    if Y==0:
       #print "insert"
       title=finduserid(N1)+'&&&'+finduserid(N2)
       findsomething.execute("select id from room")
       J3=findsomething.fetchall()
       g=len(J3)
       k=J3[g-1][0]
       ts=time.time()
       st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
       findsomething.execute("INSERT INTO room (id, create_date_time, room_type, title, version) VALUES ('%d','%s','%s','%s','%d')" % (k+1, st , "ONE_TO_ONE", title, 1))
       findsomething.execute("INSERT INTO room_members (roomid, memberid) VALUES ('%s','%s')" % (k+1, N1))
       findsomething.execute("INSERT INTO room_members (roomid, memberid) VALUES ('%s','%s')" % (k+1, N2))

PinLiang.commit()
'''
''' Have Room and Room Relationship but no Member Relationship.
print set(b)^set(c)

for x in range(len(a)):
    if (a[x][0][1]==9 and a[x][1][1]==54):
       print a[x][0][0]
'''
findsomething.close() 
PinLiang.close()


