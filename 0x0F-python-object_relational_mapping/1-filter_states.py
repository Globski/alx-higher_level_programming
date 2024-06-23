#!/usr/bin/python3
"""
Lists all states with names starting with 'N' from the database hbtn_0e_0_usa.

This script takes three arguments:
    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        db_name (str): The name of the database.
Usage:
    ./1-filter_states.py hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
