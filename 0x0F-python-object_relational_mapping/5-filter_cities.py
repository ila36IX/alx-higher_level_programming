#!/usr/bin/python3

"""

Lists all cities of that state,
based on name argument.

"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    searched = argv[4]

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
                                             WHERE s.name = %s
                                          ORDER BY c.id
                                          """, (searched, ))
    print_str = ""
    for row in c.fetchall():
        print_str += row[1] + ", "
    print(print_str[:-2])
