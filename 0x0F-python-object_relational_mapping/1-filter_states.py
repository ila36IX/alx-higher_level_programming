#!/usr/bin/python3

"""

Lists all states with a name starting with N

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
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    for row in c.fetchall():
        print(row)
