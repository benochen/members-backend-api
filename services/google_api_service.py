from exceptions.google_api_userinfo_exception import google_api_userinfo_exception
import requests
class google_api_service:

    def __init__(self,access_token):
        self.access_token=access_token
        self.root_url="https://www.googleapis.com/oauth2/v1/"
        self.user_info_route="userinfo"

    def get_user_info(self):
        complete_route=self.root_url+self.user_info_route
        headers=dict()
        headers["Authorization"]=f"Bearer {self.access_token}"
        response = requests.get(complete_route,headers=headers)
        if response.status_code !=200:
            raise google_api_userinfo_exception("")
        return response.json()


