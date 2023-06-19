#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_101_usa
Usage: ./102-relationship_cities_states_list.py root root hbtn_0e_101_usa
"""
import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


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
    # Base.metadata.bind = engine

    # Create a session to perform database operations
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects with their associated States objects
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()
