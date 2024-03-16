#!/usr/bin/python3

import sys, MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(host="localhost", 
                         user=username, 
                         password=password, 
                         database=db_name, 
                         port=3306
                    )

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id", (searched, ));

    for row in c.fetchall():
        print(row)

