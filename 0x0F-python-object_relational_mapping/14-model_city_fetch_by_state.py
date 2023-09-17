#!/usr/bin/python3
"""
Task 14 module
"""


import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database
            ),
            pool_pre_ping=True
        )
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        cities = (
                session.query(City, State)
                .join(State)
                .order_by(City.id)
                .all()
        )
        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
        session.close()
