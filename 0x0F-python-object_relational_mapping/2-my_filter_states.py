#!/usr/bin/python3

"""module print from where name = argument"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', port=3360, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    var = sys.argv[4]
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(var)
    cur.execute(query)

    q_rows = cur.fetchall()

    for i in q_rows:
        print(i)

    cur.close()
    conn.close()
