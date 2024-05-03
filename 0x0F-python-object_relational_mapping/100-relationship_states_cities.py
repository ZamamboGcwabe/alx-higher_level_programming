#!/usr/bin/python3
"""Inserts a State and City into the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State
    new_state = State(name="California")

    # Create a new City
    new_city = City(name="San Francisco")

    # Append the city to the state's list of cities
    new_state.cities.append(new_city)

    # Add new_state to the session
    session.add(new_state)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
