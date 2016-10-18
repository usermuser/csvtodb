import csv, sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS csvapp_data_csv")
#print data dropped;
#cur.execute("CREATE TABLE PCFC (id INTEGER PRIMARY KEY, type INTEGER, term TEXT, definition TEXT);")
cur.execute ("CREATE TABLE csvapp_data_csv(ID INTEGER PRIMARY KEY, name VARCHAR(100), price INTEGER);")
reader = csv.reader(open('data.csv', 'r'), delimiter=',')
for row in reader:
    #to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8")]
    cur.execute("INSERT INTO csvapp_data_csv (name, price) VALUES (?, ?);", to_db)
con.commit()