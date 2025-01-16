from .request import Request 
from .response import Response
from typing import Callable, Dict, Any 
 

class SimpleFramework:
    def __init__(self):
        self.routes: Dict[str, Dict[str, Callable]] ={} 
    
    def route(self, path: str, method: str = "GET"):
        def decorator(handler: Callable):
            if path not in self.routes:
                self.routes[path] = {}
            self.routes[path][method] = handler 
            return handler 
        return decorator
    
    async def handle_request(self, request: Request) -> Response:
        path = request.scope.get('path', '/')
        method = request.scope.get('method','GET') 

        if path not in self.routes or method not in self.routes[path]:
            return Response({"error": "Not Found"}, status=404) 

        handler = self.routes[path][method]
        return await handler(request) 
    
    async def __call__(self, scope: Dict[str,Any], receive: Callable, send: Callable):
        request = Request(scope)
        response = await self.handle_request(request) 

        await send({
            'type': 'http.response.start',
            'status': response.status,
            'headers': [
                [b'content-type', b'application/json'],
            ],
        })

        await send({
            'type': 'http.response.body',
            'body': str(response.body).encode(), 
        })