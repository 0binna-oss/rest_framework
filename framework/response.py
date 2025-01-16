class Response:
    def __init__(self, body: dict, status=200, content_type="text/plain"):
        self.body = body
        self.status = status 
        self.content_type = content_type 
    
    def build(self):
        headers = [(b"content_type", self.content_type.encode("utf-8"))]
        return {
            "status": self.status,
            "headers": headers,
            "body": self.body.encode("utf-8"),
        } 