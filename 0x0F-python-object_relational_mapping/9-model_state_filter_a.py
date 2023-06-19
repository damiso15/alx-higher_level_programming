#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
Usage: ./9-model_state_filter_a.py root root hbtn_0e_6_usa
"""
import sys
# import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py username password database")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create Logs
    # logging.basicConfig()
    # logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # Create Engine and Session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the states that contains the letter a
    states = session.query(State).filter(
                State.name.like('%a%')).order_by(State.id).all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
