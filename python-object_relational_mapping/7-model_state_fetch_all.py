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

engine = create_engine(
    f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}"
)

Session = sessionmaker(bind=engine)

session = Session()

states = session.query(State).all()

for state in states:
    print(f"{state.id}: {state.name}")

session.close()
