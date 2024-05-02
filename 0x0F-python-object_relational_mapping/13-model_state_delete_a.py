#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'
   from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State objects containing the letter 'a' in their name
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the State objects containing the letter 'a'
    for state in states_with_a:
        session.delete(state)

    # Commit the session to save the changes
    session.commit()

    # Close the session
    session.close()
