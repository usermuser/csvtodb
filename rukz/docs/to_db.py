#!/usr/bin/python
# -*- coding: utf-8 -*-e
import csv, sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS rukz_rukzak")
print ('table dropped')
#print data dropped;
#cur.execute("CREATE TABLE PCFC (id INTEGER PRIMARY KEY, type INTEGER, term TEXT, definition TEXT);")
cur.execute ("CREATE TABLE rukz_rukzak(ID INTEGER PRIMARY KEY, link VARCHAR(200), naim VARCHAR(200), price REAL, img_link VARCHAR(200), other VARCHAR(200));")
print('table created')
reader = csv.reader(open('1.csv', 'r'), delimiter=';')
for row in reader:
    #to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"), unicode(row[3], "utf8"), unicode(row[4], "utf8"),]
    cur.execute("INSERT INTO rukz_rukzak (link, naim, price, img_link, other) VALUES (?, ?, ?, ?, ?);", to_db)
    print(to_db)

con.commit()
print ('all data commited')