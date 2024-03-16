#!/usr/bin/python3

"""

State class

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """
    The State class will abstract the implementation of states table
    """
    __tablename__ = "states"

    id = Column(Integer,
                autoincrement=True,
                primary_key=True,
                unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.name}"
