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
    c.execute("""
        SELECT c.id, c.name, s.name FROM cities AS c 
                                              JOIN states AS s 
                                                ON c.state_id = s.id 
                                             WHERE s.name = %s
                                          ORDER BY c.id
                                          """, (searched, ))

    for row in c.fetchall():
        print(row)


