#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
Usage: ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
"""
import sys
import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py username password database")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create Logs
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # Create Engine and Session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the cities and their corresponding states
    # cities = session.query(City, State).filter(
    # State.id == City.state_id).order_by(City.id).all()
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Display results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
