#!/usr/bin/python3

import MySQLdb
import sys

conn = MySQLdb.connect(host='localhost', port=3360, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = conn.cursor()
cur.execute("SELECT c.`name` FROM cities AS c INNER JOIN states AS s ON c.state_id = s.id WHERE s.name = %s", (sys.argv[4],))

q_rows = cur.fetchone()

for i in q_rows:
    print(i)

cur.close()
conn.close()