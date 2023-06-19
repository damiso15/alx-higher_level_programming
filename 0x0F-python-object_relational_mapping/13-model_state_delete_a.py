#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the 
letter a from the database hbtn_0e_6_usa
Usage: ./13-model_state_delete_a.py root root hbtn_0e_6_usa
"""
import sys
import logging
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
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # Create Engine and Session
    engine = create_engine('mysql+mysqldb://{}:{}@sqldb/{}'.format(
        username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the states to delete
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the state from the session
    for state in states:
        session.delete(state)
    session.commit()

    session.close()
