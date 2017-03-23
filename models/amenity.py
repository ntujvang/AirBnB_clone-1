#!/usr/bin/python3
from models import *
from os import getenv
from sqlalchemy import Column, String, Table
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
