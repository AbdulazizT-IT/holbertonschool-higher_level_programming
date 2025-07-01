#!/usr/bin/python3
"""
Lists all rows in 'states' table where name
matches the argument.
Usage: ./2-my_filter_states.py <username>
<password> <db_name> <state_name>
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    state_name = sys.argv[4]
    query = "SELECT * \
            FROM states \
            WHERE name = %s \
            ORDER BY id ASC"

    cur.execute(query, (state_name,))
    states = cur.fetchall()

    for state in states:
        print(state)
