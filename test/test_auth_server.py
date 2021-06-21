import os, tempfile, pytest
import sys,inspect, requests
from google.auth import jwt

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from app import app
from loginRegistration import bp

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ssbu2018!@localhost:5432/jwt_auth_test"
    app.config['TESTING'] = True
    
    app.register_blueprint(bp)
    
    with app.test_client() as client:
        yield client

def test_token_maker(client):
    rv = client.get('/login?username=NotAHippo&password=Ssbu2018!')
    r = requests.get("http://localhost:5001/meshes/uploadMesh?filename=Wall3&materialID=123&type=Cube&token=" + rv.data.decode("utf-8"))
    print(r.status_code)
    assert r.status_code == 200

def test_get_meshes_csv(client):
    rv = client.get('/login?username=NotAHippo&password=Ssbu2018!')
    r = requests.get("http://localhost:5001/meshes/uploadMesh?filename=Wall3&materialID=123&type=Cube&token=" + rv.data.decode("utf-8"))
    print(r.status_code)
    assert r.status_code == 200
