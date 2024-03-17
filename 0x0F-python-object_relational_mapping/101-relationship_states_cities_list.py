#!/usr/bin/python3
"""

Querying to 1TM schema database
1 To Many relationship using mysqlalchemy

"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City, Base
from relationship_state import State

if __name__ == "__main__":
    db_str = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_str)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda x: x.id):
            print(f"\t{city.id}: {city.name}")
