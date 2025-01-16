from typing import Callable, Any, List 
from .request import Request 
from .response import Response 

SERVER_HOST = "localhost"
SERVER_PORT = 8000 


class Middleware:
    def __init__(self, app: Any):
        self.app = app 
        self.middleware_stack: List[Callable] = [] 
    
    def add_middleware(self, middleware_func: Callable):
        self.middleware_stack.append(middleware_func)
    
    async def __call__(self, scope: dict, recieve: Callable, send: Callable):
        request = Request(scope) 
        handler = self.app

        # Wrap the handler with all middlewares in reverse order 
        for middleware in reversed(self.middleware_stack):
            handler = await self._wrap_handler(middleware, handler)

        return await handler(scope, recieve, send) 
     
    async def _wrap_handler(self, middleware: Callable, handler: Callable):
        async def wrapped(scope: dict, receive: Callable, send: Callable):
            request = Request(scope)
            return await middleware(request, lambda r: handler(scope, receive, send))
        return wrapped 
    
async def logging_middleware(request: Request, call_next: Callable) -> Response:
    print(f"Request: {request.method} {request.url}") 
    response = await call_next(request)
    print(f"Response: {response.status_code}")
    return response 

__all__= ['Middleware', 'logging_middleware'] 
    