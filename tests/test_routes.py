import pytest
from app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from Flask App!"}

