from urllib.parse import parse_qs

class Request:
    def __init__(self, scope, recieve=None):
        self.scope = scope 
        self.recieve = recieve 
        self.method = scope.get('method', '') 
        self.url = self._get_url()  
        self.type = scope.get('type', '')  
        self.path = scope.get('path', '') 
        self.headers = dict(scope.get('headers', [])) 
        self.query_string = scope.get('query_string', b'').decode() 
    
    def _get_url(self) -> str:
        # Construct the full url from scope 
        scheme = self.scope.get('scheme', 'http')
        server = self.scope.get('server', ('localhost', 8000))
        host, port = server 
        path = self.scope.get('path', '/') 

        if (scheme == 'http' and port == 80) or (scheme == 'https' and port == 443):
            return f"{scheme}://{host}{path}"
        return f"{scheme}://{host}:{port}{path}"
    
    async def json(self):
        # Get the JSON body of the request
        import json 
        body = await self.body()
        return json.loads(body) if body else {} 
    
    async def body(self):
        # Get the body of the request 
        if not self.receive:
            return b''
        body = b''
        more_body = True 

        while more_body:
            message = await self.receive()
            body +=  message.get('body', b'')
            more_body = message.get('more_body', False)
        return body 