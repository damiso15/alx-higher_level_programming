#!/usr/bin/python3
"""
A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
Usage: ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
"""
import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py username password database")
        sys.exit(1)

    # Set up connection and session to the database
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create Logs
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@sqldb:3306/{}'.format(
        user, password, database), pool_pre_ping=True)

    # Bind the engine to the Base metadata
    State.metadata.bind = engine

    # Create a session to perform database operations
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects with their associated City objects
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
        cities = state.cities
        for city in cities:
            print(f"\t{city.id}: {city.name}")

    # Close the session
    session.close()
