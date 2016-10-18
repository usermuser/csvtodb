
import sqlite3 as lite
import csv

ifile = open ('data.csv',rb)

try:
  con = lite.connect('db.sqlite3')
  cur = con.cursor()
  cur = execute("DROP TABLE IF EXISTS csvapp_data_csv")
  cur = execute ("CREATE TABLE csvapp_data_csv(ID INTEGER PRIMARY KEY, name VARCHAR(100), price INTEGER)")