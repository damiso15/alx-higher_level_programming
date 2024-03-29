#!/usr/bin/env python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


# Establish a connection
conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        charset="utf8"
        )

# Performing database operations
if len(sys.argv) > 4:
    filter_word = sys.argv[4]
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER by id ASC"
    cur.execute(query, ('%' + filter_word + '%',))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
