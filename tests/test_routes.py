import pytest 
from framework.framework import Simpleframework
from framework.response import Response 
from framework.request import Request

async def test_route(request: Request) -> Response:
    return Response({"message": "Hello World"}) 

routes = {
    "/test": test_route
}

async def another_route(request: Request) -> Response:
    return Response({"data": "Another endpoint"})

routes["/another"] = another_route 