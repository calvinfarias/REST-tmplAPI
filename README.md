# RESTAPI1stTMPL
This is a REST API template project. The only requirement is that it must have an endpoint that inserts an arbitrary `key: value` pair over a request's header. It's not clear if it's in the Response's header or in the Request's header, even though it is intuitive to assume the right one is the Response's.



### INSTALLING

### USING

### APPROACH

Implement an API following the FastAPI [documentation](https://fastapi.tiangolo.com/); create an arbitrary endpoint and then insert the `key: value` pair on the header. 

For completeness sake, two endpoints were implemented. One where the changed header belongs to Response and one where the header belongs to Request.



The first endpoint is `GET /foo`. It will return a Response in the JSON format with a `{'foo': 'bar'}` content and  a `{'inserted-header': 'this value was inserted at the endpoint processing'}` header.



The second endpoint is `GET /dummy`. It will receive the Request as parameter and return the content read from the Request.headers as `{'inserted-header': 'this value was inserted within a custom route handler'}`

One more time, the FastAPI [documentation](https://fastapi.tiangolo.com/advanced/custom-request-and-route/) describes the steps needed to solve the problem. In this case it explain how to build a router that will capture the Request before it is processed at the endpoint. This allows one to change its headers. **The author fails to see the purpose of doing this, but it's done nevertheless.**

You can check the code to implement a router here:

```
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

