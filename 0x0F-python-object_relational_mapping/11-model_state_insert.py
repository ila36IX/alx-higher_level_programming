#!/usr/bin/python3

import sys
from model_state import Base, State 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__": 
    db_str = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}"
    engine = create_engine(db_str)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
