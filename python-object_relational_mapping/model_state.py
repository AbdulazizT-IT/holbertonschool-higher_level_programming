#!/usr/bin/python3
"""
Defines the State class mapped to the 'states' table.

- id: primary key, integer, not nullable
- name: string(128), not nullable
"""

import sys
import MySQLdb
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents the 'states' table in the database.

    Attributes:
    id (Integer): Primary key column,
    unique identifier for each state, not nullable.
    name (String): Name of the state,
    max length 128 characters, not nullable.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
