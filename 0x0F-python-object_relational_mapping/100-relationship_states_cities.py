#!/usr/bin/python3
"""
creates the State "California" with the City "San Francisco" from the
database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from relationship_base import Base


if __name__ == '__main__':
    # Set up connection and session to the database
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@sqldb:3306/{database}')

    # Bind the engine to the Base metadata
    Base.metadata.bind = engine

    # Create all tables
    Base.metadata.create_all(bind=engine)

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

