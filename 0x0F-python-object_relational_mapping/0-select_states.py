#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username>
                            <mysql password>
                            <database name >
"""
import sys
import MySQLdb


if __name__ == "__main__":
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
    if len(sys.argv) > 3:
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER by id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
