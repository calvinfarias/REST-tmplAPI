from fastapi import FastAPI, Request, Response
from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse

from typing import Callable

class CustomRoute(APIRoute):
    ''' This will capture the original route and change the request's header before processing it at the endpoint
    '''
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:

            injected_header: Tuple[bytes] = b'injected-header', b'this is a header value injected within a custom route handler'

            request.headers.__dict__['_list'].append(injected_header)

            return await original_route_handler(request)

        return custom_route_handler

app = FastAPI()
app.router.route_class = CustomRoute

@app.get('/dummy')
async def dummy(request: Request):
    content = {'injected-header': request.headers['injected-header']}
    return content

@app.get('/foo')
async def foo():
    content = {'foo': 'bar'}
    headers = {'injected-header': 'this is a header value injected at the endpoint processing'}
    return JSONResponse(content=content, headers=headers)

