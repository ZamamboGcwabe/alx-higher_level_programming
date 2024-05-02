#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""

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

    # Query the State object with id=2
    state = session.query(State).filter(State.id == 2).first()

    if state:
        # Change the name of the state
        state.name = "New Mexico"

        # Commit the session to save the changes
        session.commit()

    # Close the session
    session.close()
