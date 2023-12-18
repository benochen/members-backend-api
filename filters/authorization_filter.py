import logging

from exceptions.authorization_exception import authorization_exception


from services.google_api_service import google_api_service
from exceptions.google_api_userinfo_exception import google_api_userinfo_exception
import re


logger = logging.getLogger("security")
server_logger = logging.getLogger("api")

class authorization_filter:


    def __init__(self, context:dict):
        self.request = context.get("request")
        self.context=context
        self.access_token =""
        self.user_info=dict()
        self.authorized_org="asso.ecreadys.fr"

    def authorized(self):

        server_logger.info("Start authorization process",extra={"context":self.context})
        server_logger.debug("Check if authorization header is present",extra={"context":self.context})
        if not self._check_authorization_exists():
            server_logger.error("The authorization header does not exist", extra={"context": self.context})
            raise authorization_exception("The authorization header does not exist",context=self.context)
        server_logger.debug("Access token found",extra={"context":self.context})
        if not self.__check_access_token_format():
            server_logger.error("Baf format for access token", extra={"context": self.context})
            raise authorization_exception("Bad format for access token",context=self.context)
        server_logger.debug("The format of the token is valid",extra={"context":self.context})
        server_logger.debug("Start checking of the content of access token is valid",extra={"context":self.context})
        if not self.__check_access_token_validity():
            server_logger.error("Access token is not valid", extra={"context": self.context})
            raise authorization_exception("Access token is not valid",context=self.context)
        server_logger.info("Access token is valid.",extra={"context":self.context})
        if not self.__check_allowed_organization():
            email=str(self.user_info["email"])
            domain=email.split("@")[1]
            raise authorization_exception( f"Access_token generated thanks '{domain}' mail. You need to belong to the organization '{self.authorized_org}'",context=self.context)
        server_logger.info(f"User belongs to {self.authorized_org}",extra={"context":self.context})
        self.context={
            "request":self.request,
            "user":self.user_info,
            "event_sec_type": "AUTHENTICATION"
        }
        server_logger.info("Authentication successfull",extra={"context":self.context})
        logger.info(f"Authentication successfull",extra={"context":self.context})

    def _check_authorization_exists(self):
        authorization_header=self.request.headers.get("Authorization")
        return authorization_header != None

    def __check_access_token_format(self):
        authorization_header=self.request.headers.get("Authorization")
        values=authorization_header.split(" ")
        if values[0] == "Bearer" and values[1] is not "":
            self.access_token=values[1]
            return True
        else:
            return False
    def __check_access_token_validity(self):
        try:
            google_api_service_obj=google_api_service(self.access_token)
            userinfo=google_api_service_obj.get_user_info()
            self.user_info=userinfo
            return True
        except google_api_userinfo_exception as e:
            return False

    def __check_allowed_organization(self):
        email_authenticated=str(self.user_info["email"]).split("@")[1]
        pattern=f"^{email_authenticated}$"
        res=re.search(pattern,self.authorized_org)

        if res:
            return True
        else:
            return False

    def get_user_info(self):
        return self.user_info
    def __destroy_access_token(self):
        pass
