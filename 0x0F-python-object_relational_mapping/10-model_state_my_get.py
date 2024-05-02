#!/usr/bin/python3
"""Prints the id of the State object with the name passed as argument from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State object with the given state name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the id if state is found, otherwise print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
