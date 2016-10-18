#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


con = lite.connect('db.sqlite3') 



with con:    
    
    cur = con.cursor()    
    #cur.execute("SELECT * FROM csvapp_data_csv") #normal table
    cur.execute("SELECT * FROM shop_product") #temporary request

    rows = cur.fetchall()

    for row in rows:
        print row