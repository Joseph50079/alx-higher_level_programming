#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    users = session.query(State).order_by(State.id.asc()).all()
    for user in users:
        cities = session.query(City).filter_by(
            state_id=user.id).order_by(
            City.id.asc()).all()
        for city in cities:
            print("{}: ({}) {}".format(user.name, city.id, city.name))
