from fastapi.testclient import TestClient

from tmplapi import app

client = TestClient(app)

def test_endpoint_dummy():
    ''' This will execute all the endpoint dummy's tests
    '''
    response = client.get('/dummy')

    assert response.status_code == 200
    assert response.json() == {'injected-header': 'this is a header value injected within a custom route handler'}

def test_endpoint_foo():
    ''' This will execute all the endpoint foo's tests
    '''
    response = client.get('/foo')

    assert response.status_code == 200
    assert response.json() == {
            'foo': 'bar',
            'injected-header': 'this is a header value injected within a custom route handler'
    }
