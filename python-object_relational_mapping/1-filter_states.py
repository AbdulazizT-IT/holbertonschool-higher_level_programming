#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa

This script connects to a MySQL database, retrieves all the states
from the `states` table, and displays them in ascending order by `id`.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    """
    This script takes 3 arguments (mysql username, mysql password,
    and database name) and lists all states from the `states` table
    in the given database, ordered by the `id` in ascending order.
    """

    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306,
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
