import logging
import traceback
from logging.config import fileConfig
from fastapi import Request,Response

logger = logging.getLogger("security")  # the __name__ resolve to "uicheckapp.services"
                                      # This will load the uicheckapp logger

class authorization_exception(Exception):

    def __init__(self,message,context):
        self.message=message
        super().__init__(self.message)
        self.log_security(message,context)

    def log_security(self,message,context:dict="test"):
        try:
            context=context.update({"sec_event_type":"AUTHENTICATION"})
            print(context)
            logger.error(message,extra={"context": context})
        except Exception as e:
            traceback.print_exc()

