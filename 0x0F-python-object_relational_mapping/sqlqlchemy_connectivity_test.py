#!/usr/bin/env python3

import sys
import logging
from sqlalchemy import create_engine

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py username password database")
        sys.exit(1)
        
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@192.168.127.23/{database}', pool_pre_ping=True)
    connection = engine.connect()
    connection.close()
    print("Connection successful!")

