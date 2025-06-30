#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                        db=sys.argv[3], port=3306)

    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)
    states = cursor.fetchall()
    
    for state in states:
        print(state)