#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.

This script takes four arguments:
    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        db_name (str): The name of the database.
        state_name (str): The name of the state to search for.

Usage:
    ./2-my_filter_states.py hbtn_0e_0_usa 'Arizona'
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states "
    WHERE name LIKE BINARY '{}' "
    "ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    cur.close()
    db.close()
