#!/usr/bin/python3
"""
Task5 module for mysql task
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) == 5:
        username = argv[1]
        password = argv[2]
        database = argv[3]
        state_name = argv[4]
        conn = MySQLdb.connect(
          host="localhost",
          port=3306,
          user=username,
          passwd=password,
          db=database,
          charset="utf8",
        )
        cur = conn.cursor()
        query = "SELECT cities.name FROM cities \
JOIN states ON state.id = cities.states_id WHERE states.name = %s \
ORDER BY cities.id ASC", (state_name,)
        cur.execute(query)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
