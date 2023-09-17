#!/usr/bin/python3
"""
Task 13 module
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
        states_to_delete = (
                session.query(State)
                .filter(State.name.like('%a%'))
                .all()
        )
        if states_to_delete:
            for state in states_to_delete:
                session.delete(state)
            session.commit()
        else:
            print("No states found to delete")
        session.close()
