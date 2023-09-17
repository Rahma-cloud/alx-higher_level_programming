#!/usr/bin/python3
"""
Task 11 module
"""


import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database
            ),
            pool_pre_ping=True
        )
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print(new_state.id)
        session.close()
