#!/usr/bin/python3

"""

Lists all cities from the database

"""


import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         password=password,
                         database=db_name,
                         port=3306
                         )

    c = db.cursor()
    c.execute("""
        SELECT c.id, c.name, s.name FROM cities AS c
                                              JOIN states AS s
                                                ON c.state_id = s.id
                                          ORDER BY c.id
                                          """)

    for row in c.fetchall():
        print(row)
