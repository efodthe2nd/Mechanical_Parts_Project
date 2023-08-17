#!/usr/bin/python3
'''database storage engine'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.part import Part
from models.base_model import Base
from models.generator import Generator
from models.manufacturer import Manufacturer
from os import getenv

classes = {"Part": Part, "Generator": Generator,
           "Manufacturer": Manufacturer}

class DBStorage:
  '''database storage engine for mysql storage'''
  __engine = None
  __session = None

  def __init__(self):
    '''Instantiate new dbstorage instance'''
    MECH_MYSQL_USER = getenv('MECH_MYSQL_USER')
    MECH_MYSQL_PWD = getenv('MECH_MYSQL_PWD')
    MECH_MYSQL_HOST = getenv('MECH_MYSQL_HOST')
    MECH_MYSQL_DB = getenv('MECH_MYSQL_DB')
    MECH_ENV = getenv('MECH_ENV')
    self.__engine = create_engine(
      'mysql+mysqldb://{}:{}@{}/{}'.format(
                                      MECH_MYSQL_USER,
                                      MECH_MYSQL_PWD,
                                      MECH_MYSQL_HOST,
                                      MECH_MYSQL_DB
                                    ), pool_pre_ping=True)
  def all(self, cls=None):
    '''query on the curreent db session all cls objects'''
    dct = {}
    if cls is None:
      for c in classes.values():
        objs = self.session.query(c).all()
        for obj in objs:
          key = obj.__class__.__name__ + '.' + obj.id
          dct[key] = obj
    else:
      objs = self.__session.query(cls).all()
      for obj in objs:
        key = obj.__class__.__name__+ '.' + obj.id
        dct[key] = obj
    return dct

  def new(self, obj):
    '''adds the obj to the current db session'''
    if obj is not None:
      try:
        self.__session.add(obj)
        self.__session.flush()
        self.__session.refresh(obj)
      except Exception as ex:
        self.__session.rollback()
        raise ex
  
  def save(self):
    '''commits all changes of the current db session '''
    self.__session.commit()

  def delete(self, obj=None):
    '''deletes from the current database session on the obj'''
    if obj is not None:
      self.__session.query(type(obj)).filter(
          type(obj).id == obj.id).delete()

  def reload(self):
    '''reloads the database'''
    Base.metadata.create_all(self.__engine)
    session_factory = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
    self.__session = scoped_session(session_factory)()

  def close(self):
    '''closes the working SQLALchemy session'''
    self.__session.close()
