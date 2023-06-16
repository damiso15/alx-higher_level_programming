#!/usr/bin/env python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


# Establish a connection
conn = MySQLdb.connect(
        host="sqldb",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        charset="utf8"
        )

# Performing database operations
if len(sys.argv) > 3:
    cur = conn.cursor()
    select_query = "SELECT cities.id, cities.name, states.name "
    from_query = "FROM cities, states "
    where_query = "WHERE cities.state_id = states.id "
    order_query = "ORDER BY cities.id ASC"
    full_query = select_query + from_query + where_query + order_query
    cur.execute(full_query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
