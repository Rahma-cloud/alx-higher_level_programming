#!/usr/bin/python3
"""
Task0 module
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
        cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY \
		'N%' ORDER BY id ASC"
        )
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
