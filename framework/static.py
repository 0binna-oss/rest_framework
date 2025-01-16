import os 

class StaticFiles:
    def __init__(self, directory):
        self.directory = directory 
    
    async def __call__(self, scope, recieve, send):
        path = scope["path"].Lstrip("/")
        file_path = os.path.join(self.directory, path)

        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                content = file.read()
            await send({
                "type": "http.response.start",
                "status": 200,
                "headers": [(b"content-type", b"text/plain")]
            })
            await send({
                "type": "http.response.body",
                "body": content
            })
        else:
            await send({
                "type": "http.response.start",
                "status": 404,
                "headers": [(b"content-type", b"text/plain")]
            })
            await send({
                "type": "http.response.body",
                "body": b"404 Not Found" 
            })