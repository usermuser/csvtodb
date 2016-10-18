#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv, sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS rukz_rukzak")
print ('table dropped')
#cur.execute ("CREATE TABLE rukz_rukzak(ID INTEGER PRIMARY KEY, link VARCHAR(200), naim VARCHAR(200), price REAL, img_link VARCHAR(200), other VARCHAR(200));")
#cur.execute ("CREATE TABLE rukz_rukzak(ID INTEGER PRIMARY KEY, link VARCHAR(200), naim VARCHAR(200));")
cur.execute ("CREATE TABLE rukz_rukzak(ID INTEGER PRIMARY KEY, naim VARCHAR(200), price REAL);")
print('table created')
#reader = csv.reader(open('data.csv', 'r'), delimiter=',')
reader = csv.reader(open('rukzak_test.csv', 'r'), delimiter=';')
for row in reader:
    
    #to_db = [(row[0], "utf8"), (row[1], "utf8"), (row[2], "utf8"), (row[3], "utf8"), (row[4], "utf8"),]
    #to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8")]
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8")]
    #cur.execute("INSERT INTO rukz_rukzak (link, naim, price, img_link, other) VALUES (?, ?, ?, ?, ?);", to_db)
    cur.execute("INSERT INTO rukz_rukzak (naim, price) VALUES (?, ?);", to_db)
    print(to_db)

con.commit()
print ('all data commited')