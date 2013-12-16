#Author:PinLiang, Chen
#Date:16/12/2013
#!/usr/bin/python
import MySQLdb
import mysql.connector

PinLiang=mysql.connector.connect(host='127.0.0.1', user='yourname', passwd='yourpasswd', db='yourdb', buffered=True)

findsomething = PinLiang.cursor()

findsomething.__class__

findsomething.execute("select * from yourtable")

row=findsomething.fetchall()

for x in range(80):
	findsomething.execute("INSERT INTO peers (id,name,mailbox, username, cid_number, secret, macaddress, label) VALUES ('%d','%s','%s','%s','%s','%s','%s','%s')" % (row[x][0],row[x][12],row[x][12],row[x][12],row[x][12],row[x][9],row[x][12],row[x][12]))

PinLiang.commit()

findsomething.close()

PinLiang.close()
