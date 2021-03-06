from fastapi.testclient import TestClient

from tmplAPI.tmpl import app

client = TestClient(app)

def test_endpoint_dummy():
    ''' This will execute all the endpoint dummy's tests
    '''
    response = client.get('/dummy')

    assert response.status_code == 200
    assert response.json() == {'inserted-header': 'this value was inserted within a custom route handler'}

def test_endpoint_foo():
    ''' This will execute all the endpoint foo's tests
    '''
    response = client.get('/foo')

    assert response.status_code == 200
    assert response.headers['inserted-header'] == 'this value was inserted at the endpoint processing'
    assert response.json() == {'foo': 'bar'}
