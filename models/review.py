#!/usr/bin/python3
from models import *
from os import getenv
from sqlalchemy import Column, String, Table, ForeignKey
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
