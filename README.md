

# REST tmplAPI
[![License](https://img.shields.io/badge/license-MIT-black.svg)](../master/LICENSE)
![Language](https://img.shields.io/badge/language-Python-blue.svg)

This is a REST API made for a specific task. The only requirement is that it must have an endpoint that inserts an arbitrary `key: value` pair over a request's header. It's unclear if it's in the Response's header or the Request's header, even though it is intuitive to assume it's the former.

This repository will remain as a template for future references / FastAPI developments.


### INSTALLING

You can install it by running 
``` bash
# create and activate a virtual environment
python -m venv venv && source venv/bin/activate

# you may want to update your pip version
python -m pip install --upgrade pip

# install the tmplAPI from this github account
pip install git+https://github.com/calvinfarias/REST-tmplAPI
```



### TESTING

You can check if everything is properly installed by moving into the test directory and running `pytest`
``` bash
# access the test folder inside the path for which you installed tmplAPI
# pay attention to the python version you are using. In this example it's 3.8.*
cd venv/lib/python3.8/site-packages/tmplAPI/tests/

# and execute pytest
pytest
```



### USING

You can import the FastAPI application from tmplAPI.tmpl and execute it with uvicorn
``` Python
from tmplAPI.tmpl import app
import uvicorn

uvicorn.run(app, host='0.0.0.0', port=8000, reload=False)
```

and run the requests to the server

``` bash
curl -X 'GET' \
  'http://0.0.0.0:8000/dummy' \
  -H 'accept: application/json'
```

and

``` bash
curl -X 'GET' \
  'http://0.0.0.0:8000/foo' \
  -H 'accept: application/json'
```

FastAPI also offers automatic documentation, you can check it on http://0.0.0.0:8000/docs



### APPROACH

Implement an API following the FastAPI [documentation](https://fastapi.tiangolo.com/); create an arbitrary endpoint and then insert the `key: value` pair on the header. 

For completeness sake, two endpoints were implemented. One where the changed header belongs to Response and one where the header belongs to Request.


The first endpoint is `GET /foo`. It will return a Response in the JSON format with a `{'foo': 'bar'}` content and  a `{'inserted-header': 'this value was inserted at the endpoint processing'}` header.

The second endpoint is `GET /dummy`. It will receive the Request as parameter and return the content read from the Request.headers as `{'inserted-header': 'this value was inserted within a custom route handler'}`

The FastAPI [documentation](https://fastapi.tiangolo.com/advanced/custom-request-and-route/) describes the steps needed to solve the problem. In this case it explain how to build a router that will capture the Request before it is processed at the endpoint. This allows one to change its headers.

You can check the class that implements a custom router below:

``` Python
class CustomRoute(APIRoute):
     ''' This will capture the original route and change its header before processing it at the endpoint
     '''
     def get_route_handler(self) -> Callable:
         original_route_handler = super().get_route_handler()
 
         async def custom_route_handler(request: Request) -> Response:
             request['headers'].append(('key', 'value'))
             return await original_route_handler(request)
 
         return custom_route_handler
```

