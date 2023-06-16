#!/usr/bin/env python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
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
if len(sys.argv) > 3:
    filter_word = sys.argv[4]
    cur = conn.cursor()
    select_query = "SELECT cities.name "
    from_query = "FROM cities, states "
    where_query = "WHERE cities.state_id = states.id "
    and_query = "AND states.name LIKE %s "
    order_query = "ORDER BY cities.id ASC"
    full_query = select_query + from_query + where_query + and_query + order_query
    cur.execute(full_query, ('%' + filter_word + '%',))
    query_rows = cur.fetchall()
    query_list = []
    for row in query_rows:
        query_list.append(row[0])
    query_string = ", ".join(query_list)
    print(query_string)
    cur.close()
    conn.close()
