#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import PlaceAmenity, Place
from models.review import Review
from models.user import User
from sqlalchemy.orm.scoping import scoped_session


class DBStorage:
    __engine = None
    __session = None

    classes = {"Amenity": Amenity, "City": City, "State": State,
               "Place": Place, "Review": Review, "User": User}

    def __init__(self):
        usr = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_MYSQL_ENV')

        db_str = "mysql+mysqldb://{}:{}@{}/{}".format(usr, pwd, host, db)

        self.__engine = create_engine(db_str)
        Session = sessionmaker(bind=self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = Session()
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objs = {}
        if cls is None:
            for name  in self.classes.items():
                for instance in self.__session.query(eval(name)):
                    objs[instance.id] = instance
        else:
            for instance in self.__session.query(eval(cls)):
                objs[instance.id] = instance
        return objs

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        self.__session.remove()
