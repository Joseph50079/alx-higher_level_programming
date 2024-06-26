#!/usr/bin/python3

import MySQLdb
import sys

conn = MySQLdb.connect(host='localhost', port=3360, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

q_rows = cur.fetchall()

for i in q_rows:
    print(i)

cur.close()
conn.close()