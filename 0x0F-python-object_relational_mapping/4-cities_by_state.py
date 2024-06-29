#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', port=3360, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT c.`id`, c.`name`, s.`name` FROM cities AS c INNER JOIN states AS s ON c.state_id = s.id ORDER BY id",)

    q_rows = cur.fetchall()

    for i in q_rows:
        print(i)

    cur.close()
    conn.close()
