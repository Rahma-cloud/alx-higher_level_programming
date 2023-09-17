#!/usr/bin/python3
"""
Task 9 module
"""


import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) == 4:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
            ),
            pool_pre_ping=True
        )
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        states_with_a = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .order_by(State.id)
            .all()
        )
        if states_with_a:
            for state in states_with_a:
                print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")
        session.close()
