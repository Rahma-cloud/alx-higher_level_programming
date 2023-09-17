#!/usr/bin/python3
"""
Task 10 module
"""


import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database
            ),
            pool_pre_ping=True
        )
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        state = (
            session.query(State)
            .filter(State.name == state_name)
            .first()
        )
        if state:
            print(state.id)
        else:
            print("Not found")
        session.close()
