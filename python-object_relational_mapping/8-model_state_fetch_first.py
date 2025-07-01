#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.

Usage:
    ./7-model_state_fetch_all.py <mysql username>
    <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           )
    Session = sessionmaker(bind=engine)

    session = Session()
    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    session.close()
    