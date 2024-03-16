#!/usr/bin/python3

"""

Prints the first State object from the
database hbtn_0e_6_usa

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

    first_row = session.query(State).order_by(State.id).first()

    if first_row:
        print(f"{first_row.id}: {first_row.name}")
    else:
        print("Nothing")
