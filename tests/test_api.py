import pytest
from app.api import app


def test_api(client):
    response = client.get("/")
    status_code = response.status_code
    assert status_code == 200


def test_api_404(client):
    response = client.get('/api/v1/404')
    assert 404 == response.status_code


def test_statistics_endpoint_wrong_date_format(client):
    response = client.get('/api/v1/stackstats?since=2020/10/02 10:00:00')
    assert 400 == response.status_code

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
