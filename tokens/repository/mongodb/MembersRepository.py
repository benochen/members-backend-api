from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

import mongoengine
from logzero import logger

from tokens.repository.mongodb.AbstractRepository import AbstractRepository
from models.mongodb.membersDocument import MembersDocument
from mongoengine import *
T = TypeVar('T')

class MembersRepository(AbstractRepository):

    def __init__(self,host:str,port:int,db:str):
        super().__init__(host,port,db)


    def findAll(self)->List:
        try:
            self.open_connect()
            logger.debug("Start quering with findAll")
            res=list()
            for iterable_object in MembersDocument.objects():
                logger.debug(f"iterable_object={iterable_object}")
                res.append(iterable_object)
            logger.debug("Collection entity correctly loaded")
            self.close_mongo_connect()
            return res
        except Exception as e:
            print(e)

    def findOne(self,*args: T)->MembersDocument:
        email=args[0]
        if email is None:
            raise TypeError("Invalid argument provided for find one")
        logger.debug("Start searching entity with email="+email)
        self.open_connect()
        if MembersDocument.objects(email=email).count()>0:
            logger.debug("object with name="+email+" found")
            res=MembersDocument.objects(name=email).first()
        else:
            logger.debug("object with email=" + email + "not found")
            res=None
        self.close_mongo_connect()
        return res


    def insert(self,*args:T)->None:
        self.open_connect()
        if(MembersDocument.objects(Q(email=args[0].email) & Q(adhesion_name=args[0].adhesion_name)).count()==0):
            args[0].save()
        self.close_mongo_connect()


    def create(self,item: T)->None:
        pass

