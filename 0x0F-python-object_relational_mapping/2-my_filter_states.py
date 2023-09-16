#!/usr/bin/python3
"""
Task0 module
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
