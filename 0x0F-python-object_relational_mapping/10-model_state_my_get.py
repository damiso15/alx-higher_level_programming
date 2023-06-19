#!/usr/bin/python3
"""
A script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
Usage: ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
"""
import sys
# import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py username password database search")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    filter_state = sys.argv[4]

    # Create Logs
    # logging.basicConfig()
    # logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # Create Engine and Session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the states that contains the letter a
    state = session.query(State).filter(
            State.name == filter_state).order_by(State.id).first()

    # Display results
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
