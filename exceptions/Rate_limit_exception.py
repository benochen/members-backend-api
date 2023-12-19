import logging
import traceback
from logging.config import fileConfig
from fastapi import Request, Response, HTTPException
from slowapi.errors import  RateLimitExceeded
from starlette.responses import JSONResponse

logger = logging.getLogger("security")  # the __name__ resolve to "uicheckapp.services"
                                      # This will load the uicheckapp logger


def _rate_limit(request: Request, exc: RateLimitExceeded) -> Response:
    print("Raise exception")
    context=dict()
    context["request"]=request
    context["event_sec_type"]="RATE_LIMLITNG_EXCEED"


    log_security(f"Too much request : {exc.detail}",context)
    response = JSONResponse(
        {"data":"Server error","status":500}, status_code=500
    )
    response = request.app.state.limiter._inject_headers(
        response, request.state.view_rate_limit
    )
    return response



def log_security(message,context:dict="test"):
    try:

        logger.error(message,extra={"context": context})
    except Exception as e:
            traceback.print_exc()

