#!/usr/bin/python3

"""

testing

"""
import sys, MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", 
                         user=username, 
                         passwd=password, 
                         db=db_name, 
                         port=3306
                    )
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")

    for row in c.fetchall():
        print(row)
