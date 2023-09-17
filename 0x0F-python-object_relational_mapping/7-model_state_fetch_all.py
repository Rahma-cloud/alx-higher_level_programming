#!/usr/bin/python3
"""Task 7 module
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    if len(argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        hbtn_0e_6_usa = sys.argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/ \
{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        for state in session.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))
        session.close()
