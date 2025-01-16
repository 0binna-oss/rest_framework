from framework.framework import SimpleFramework
from framework.response import Response 
from framework.request import Request

app = SimpleFramework() 

@app.route("/", method="GET")
async def home(request: Request) -> Response:
    return Response("Welcome to the REST Framework!")

@app.route("/about", method="GET")
async def about(request: Request) -> Response: 
    return Response("Hello, World!")  