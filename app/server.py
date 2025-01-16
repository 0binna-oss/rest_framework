import sys
import os 
import uvicorn 
from app.app import app
from framework.response import Response 
from framework.request import Request 
from framework.middleware import Middleware  
from framework.static import StaticFiles 
from framework.middleware import logging_middleware 
from framework.static import StaticFiles

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


static_app = StaticFiles(directory="static")
middleware = Middleware(app) 
middleware.add_middleware(logging_middleware) 

async def composite_app(scope: dict, receive, send):
    if scope["type"] != "http":
        return 
    
    path = scope.get("path", "")
    if path.startswith("/static"):
        return await static_app(scope, receive, send) 
    return await middleware(scope, receive, send)

if __name__ == "__main__":
    uvicorn.run(
        composite_app,
        host = "127.0.0.1",
        port = 8000 
    )