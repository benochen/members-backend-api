from fastapi import FastAPI,Response,status,Request
def get_all_headers(request:Request):
    print(request.headers)