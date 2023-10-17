from exceptions.authorization_exception import authorization_exception
from fastapi.security import OAuth2PasswordBearer
from services.google_api_service import google_api_service
from exceptions.google_api_userinfo_exception import google_api_userinfo_exception
import re
class authorization_filter:

    def __init__(self, request):
        self.request = request
        self.access_token =""
        self.user_info=dict()
        self.authorized_org="asso.ecreadys.fr"
    def authorized(self):
        print("authorized")
        if not self._check_authorization_exists():
            print("raise exception")
            raise authorization_exception("The authorization header does not exist")
        print("check format")
        if not self.__check_access_token_format():
            raise authorization_exception("Bad format for access token")
        print(f"extract access token:{self.access_token}")
        if not self.__check_access_token_validity():
            raise authorization_exception("Access token is not valid")
        print(self.user_info)
        if not self.__check_allowed_organization():
            email=str(self.user_info["email"])
            domain=email.split("@")[1]
            print("organization check failed")
            raise authorization_exception( f"Access_token generated thanks '{domain}' mail. You need to belong to the organization '{self.authorized_org}'")
        print("Organization authorized")
    def _check_authorization_exists(self):
        authorization_header=self.request.headers.get("Authorization")
        print(authorization_header)
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
            print(e)
            return False

    def __check_allowed_organization(self):
        print("begin method")
        email_authenticated=str(self.user_info["email"]).split("@")[1]
        print("pattern to bedefined")
        pattern=f"^{email_authenticated}$"
        print(f"pattern {pattern} to search")
        res=re.search(pattern,self.authorized_org)

        if res:
            print("pattern match")
            return True
        else:
            print("pattern match failed")
            return False


    def __destroy_access_token(self):
        pass
