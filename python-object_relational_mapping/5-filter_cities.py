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

    state_name = sys.argv[4]
    cur = db.cursor()
    query = "SELECT cities.name \
    FROM cities \
    INNER JOIN states ON cities.state_id = states.id \
    WHERE states.name LIKE BINARY '{}%' \
    ORDER BY cities.id ASC".format(state_name)
    cur.execute(query)

    cities = cur.fetchall()
    # Fetch and print results
    print(", ".join(city[0] for city in cities))
