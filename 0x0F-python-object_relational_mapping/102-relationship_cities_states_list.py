#!/usr/bin/python3
"""Lists all City objects from the database"""

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

    # Query all City objects and their corresponding State objects
    cities = session.query(City).order_by(City.id).all()

    # Loop through each city
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
