#!/usr/bin/python3

"""

Prints the State object with the name passed as argument

"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    db_str = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_str)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    founded = session.query(State).\
        filter(State.name == argv[4]).\
        order_by(State.id).first()

    if founded:
        print(founded.id)
    else:
        print("Not found")
