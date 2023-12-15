
from tools.transformers import transformers
import os
import requests

class hello_asso_repository:


    def __init__(self,config_api):
        self.refresh_token=self._load_refresh_token_from_env(config_api["refresh_token_file"])
        self.scheme=config_api["scheme"]
        self.host=config_api["host"]
        self.api_version=config_api["api_version"]
        self.org_slug=config_api["org_slug"]
        self.client_id=config_api["client_id"]
        self.refresh_token_api_route=config_api["refresh_token_route"]
        self.route_organizations=config_api["route_organization"]
        self.route_forms=config_api["route_form"]
        self.route_orders=config_api["route_orders"]



    def _load_access_token(self):
        token_route_url=self.scheme+"://"+self.host+"/"+self.refresh_token_api_route
        data={
            'client_id':self.client_id,
            'refresh_token':self.refresh_token,
            'grant_type':'refresh_token'
        }
        self.my_logger.debug(f"Access token request with POST request to url {token_route_url} with client_id={self.client_id} and data={data},",activity="list-members")

        r=requests.post(token_route_url,data)

        if r.status_code==200:
            self.my_logger.info("The request succeed with code 200",activity="list-members")
            json_body=r.json()
            if "access_token" in json_body:
                self.my_logger.info("An access token has been successfully returned by the endpoint",activity="list-members")
                return json_body["access_token"]
        else:
            self.my_logger.error(f"The server respond with statuscode={r.status_code}",activity="list-members")
            self.my_logger.debug(f"debug:{r.text}",activity="list-members")
            exit()

    def _load_refresh_token_from_env(self,refresh_token_path):
        self.my_logger.debug(f"Check if {refresh_token_path} exists",activity="list-members")
        if not os.path.exists(refresh_token_path):
            self.my_logger.error(f"The file {refresh_token_path} containing refresh token does not exists",activity="list-members")
            exit(1)
        self.my_logger.info(f"The file {refresh_token_path} exists. ",activity="list-members")
        f = open(refresh_token_path,"r")
        refresh_token=f.read()
        f.close()

        if len(refresh_token) ==0 :
            self.my_logger.error(f"No refresh token in {refresh_token_path}",activity="list-members")
            exit(1)
        self.my_logger.info(f"Refresh token loaded from {refresh_token_path}",activity="list-members")
        return refresh_token

    def get_members(self,membershipslug):
        access_token=self._load_access_token()
        options="?pageIndex=1&pageSize=100&withDetails=True&sortOrder=Desc"
        complete_url=self.scheme+"://"+self.host+"/"+self.api_version+"/"+self.route_organizations+"/"+self.org_slug+"/"+self.route_forms+"/Membership"+"/"+membershipslug+"/orders"+options
        headers={
            "authorization":"Bearer "+access_token
        }
        self.my_logger.debug(f"Get members by requesting {complete_url} with headers={headers}",activity="list-members")
        r=requests.get(complete_url,headers=headers)

        if r.status_code == 200:
            self.my_logger.info("Request succeed",activity="list-members")
            transformer=transformers(r.json())
            standard_json=transformer.transform_hello_asso_to_standard_json()
            return standard_json
        else:
            self.my_logger.error(f"Request failed with status code {r.status_code}",activity="list-members")
            self.my_logger.error(f"Error details : {r.text}",activity="list-members")
            exit(1)