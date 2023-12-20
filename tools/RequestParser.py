from fastapi import FastAPI,Response,status,Request
def get_all_headers(request:Request):
    print(request.headers)

def get_real_ip(request:Request):
    headers=request.headers
    real_ip="N/A"
    for k,v in headers.items():
        if k == "x-forwarded-for":
            real_ip=v
            break
        if k =="x-real-ip":
            real_ip=v
            break
    return real_ip
