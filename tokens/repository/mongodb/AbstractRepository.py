from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
import mongoengine
from logzero import logger
T = TypeVar('T')

class AbstractRepository():


    def __init__(self,host:str,port:int,db:str):
        self.db=db
        self.host=host
        self.port=port
        self.connection_string=self.host+":"+self.port
        self.alias="default"


    @abstractmethod
    def connect(self,alias:str)->None:
        pass

    @abstractmethod
    def findAll(self)->List:
        pass
    @abstractmethod
    def findOne(self,*args: T):
        pass

    def create(self,item: T)->None:
        pass

    def disconnect(self,alias:str)->None:
        pass

    def open_connect(self,)->T:
        logger.debug("open connection to db="+self.db+";alias="+self.alias+";host="+self.host+";port="+self.port)
        return mongoengine.connect(self.db,alias=self.alias,host=self.connection_string)

    def close_mongo_connect(self)->None:
        mongoengine.disconnect(alias=self.alias)
        logger.debug("Close connection with alias=" + self.alias)