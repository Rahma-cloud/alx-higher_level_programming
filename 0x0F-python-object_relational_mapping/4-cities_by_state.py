#!/usr/bin/python3
"""
Task4 module for mysql task
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        database = argv[3]
        conn = MySQLdb.connect(
          host="localhost",
          port=3306,
          user=username,
          passwd=password,
          db=database,
          charset="utf8",
        )
        cur = conn.cursor()
        query = "SELECT cities.id, cities.name, states.name FROM cities \
JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
        cur.execute(query)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
