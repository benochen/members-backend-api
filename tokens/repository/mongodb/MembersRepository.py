import logging
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

import mongoengine
from logzero import logger

from tokens.repository.mongodb.AbstractRepository import AbstractRepository
from models.mongodb.membersDocument import MembersDocument
from mongoengine import *
T = TypeVar('T')

server_logger=logging.getLogger("api")
class MembersRepository(AbstractRepository):

    def __init__(self,host:str,port:int,db:str,context=None):
        super().__init__(host,port,db)
        self.context=context


    def findAll(self)->List:
        try:
            server_logger.info("Start requesting mongodB for all members",extra={"context": self.context})
            self.open_connect()
            server_logger.debug("Connection to mongoDB successfully opened",extra={"context": self.context})
            res=list()
            for iterable_object in MembersDocument.objects():
                res.append(iterable_object)
            self.close_mongo_connect()
            server_logger.debug("Connection to mongoDB successfiully closed",extra={"context": self.context})
            if len(res) >0:
                server_logger.info(f"{len(res)} members have been found",extra={"context":self.context})
            else:
                server_logger.info(" No member found. {] returned",extra={"context":self.context})
            return res
        except Exception as e:
            print(e)
            server_logger.error("Error during process",extra={"context":self.context,"exception":e})

    def findOne(self,*args: T)->MembersDocument:
        email=args[0]
        if email is None:
            raise TypeError("Invalid argument provided for find one")
        self.open_connect()
        if MembersDocument.objects(email=email).count()>0:
            res=MembersDocument.objects(name=email).first()
        else:
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

