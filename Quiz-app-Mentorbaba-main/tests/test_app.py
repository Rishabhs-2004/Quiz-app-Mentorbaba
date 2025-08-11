import pytest 
from app import app 
 
@pytest.fixture 
def client(): 
    app.config['TESTING'] = True 
    return app.test_client() 
 
def test_home(client): 
    rv = client.get('/') 
    assert rv.status_code == 302 
