from fastapi import FastAPI,Response,status,Request
from logzero import logger
from tokens.repository.membership.mockup_repository import mockup_repository
from tokens.repository.membership.mongo_repository import mongo_repository
from fastapi.middleware.cors import CORSMiddleware
from exceptions.authorization_exception import authorization_exception
from tools.config_parser import config_parser
from tools.transformers.transformers import Transformers
from filters.authorization_filter import authorization_filter
import exceptions
app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/my-first-api")
def hello(name: str):
  return {'Hello ' + name + '!'}

# Press the green button in the gutter to run the script.
@app.get("/membership/members")
def get_members(request:Request,response:Response):
    response_body=dict()
    try:
        auth_filter=authorization_filter(request)
        auth_filter.authorized()
        members=list()
        config="./config.ini"
        config_p = config_parser(config)
        member_rep=mongo_repository(config_p.parse_config_mongo(),"adhesion-2023-2024")
        members=member_rep.find_all()

        response_body["data"]=members
        response_body["status"]=status.HTTP_200_OK
    except authorization_exception as e:
        response.status_code=status.HTTP_401_UNAUTHORIZED
        response_body["data"]=e.message
        response_body["status"]=status.HTTP_401_UNAUTHORIZED
    except exceptions as e:
        response.status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        response.body["data"]="An exception occurs"
        response.status=status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return response_body





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
