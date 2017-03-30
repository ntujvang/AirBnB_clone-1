#!/usr/bin/python3
from models import *
from os import getenv
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship, backref
from models.base_model import BaseModel, Base
import models


class State(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE', '') != 'db':
        @property
        def cities(self):
            city = []
            states_city = models.storage.all("City")
            for c_id in states_city:
                if states_city[c_id].state_id == self.id:
                    city.append(states_city[c_id])
            return city
