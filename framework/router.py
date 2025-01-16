class Router:
    def __init__(self):
        self.routers = {}

    def add_route(self, path, method, handler):
        self.routes[(path, method)] = handler
    
    def match_route(self, path, method):
        return self.routes.get((path, method)) 