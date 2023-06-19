#!/usr/bin/python3
"""
creates the State "California" with the City "San Francisco" from the
database hbtn_0e_100_usa: (100-relationship_states_cities.py)
Usage: ./100-relationship_states_cities.py root root hbtn_0e_100_usa
"""
import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, password, database), pool_pre_ping=True)

    # Bind the engine to the Base metadata
    Base.metadata.create_all(engine)

    # Create a session to perform database operations
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create California state and San Francisco city
    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    # Add the objects to the session and commit the changes to the database
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close the session
    session.close()
