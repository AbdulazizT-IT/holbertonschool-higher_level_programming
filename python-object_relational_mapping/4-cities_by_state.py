#!/usr/bin/python3
"""
Lists all cities with their corresponding states using INNER JOIN.

Usage:
    ./script.py <username> <password> <database>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
    FROM cities \
    INNER JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id ASC"
    cur.execute(query)

    # Fetch and print results
    for city in cur.fetchall():
        print(city)
