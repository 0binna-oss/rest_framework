 Python REST Framework
A lightweight, ASGI-compliant REST framework built in Python that makes it easy to create web APIs. This framework provides a simple and intuitive way to define routes and handle HTTP requests.
Features

ASGI compatibility
Simple routing system with decorators
Request and Response handling
Support for different HTTP methods
Easy-to-use middleware system
Built-in URL parsing

Installation

Clone this repository:

bash
git clone <your-repository-url>
cd rest_framework

Install required dependencies:

bash
pip install uvicorn

Quick Start
Here's a simple example of how to create an API:
python
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

    Running the Server
To run your application:
bash
uvicorn app:app --reload
This will start the development server at http://localhost:8000

Core Components
SimpleFramework
The main framework class that handles routing and request processing.
Request
Handles incoming HTTP requests and provides easy access to request data:

Query parameters
Headers
URL parsing
Request body

Response
Handles HTTP responses with support for:

Status codes
Headers
Content type
Response body

Contributing
Feel free to submit issues and enhancement requests!
