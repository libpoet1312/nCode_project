import pathlib
import pytest
import connexion
from connexion.exceptions import InvalidSpecification
from connexion.spec import canonical_base_path

APP_FOLDER = pathlib.Path(__file__).parent.parent


def test_invalid_schema_file_structure():
    with pytest.raises(InvalidSpecification):
        connexion.FlaskApi(
            APP_FOLDER / "tests" / "INVALID_openapi3.0.yaml",
            base_path="/api/v1",
            debug=True,
        )


def test_canonical_base_path():
    assert canonical_base_path("") == ""
    assert canonical_base_path("/") == ""
    assert canonical_base_path("/api") == "/api"
    assert canonical_base_path("/api/") == "/api"


def test_api():
    app = connexion.FlaskApp(__name__, specification_dir='')
    api = app.add_api(
        APP_FOLDER / 'nCode_openapi3.0.yaml',
        base_path='/api/v1',
        options={"swagger_ui": True, "serve_spec": True},
        validate_responses=True
    )
    assert api.blueprint.name == "/api/v1"


def test_api_404(client):
    response = client.get('/api/v1/404')
    assert 404 == response.status_code


def test_statistics_endpoint_wrong_date_format(client):
    response = client.get('/api/v1/stackstats?since=2020/10/02 10:00:00')
    assert 400 == response.status_code


@pytest.fixture()
def connection_app():
    app = connexion.FlaskApp(__name__, specification_dir='')
    app.add_api(
        APP_FOLDER / 'nCode_openapi3.0.yaml',
        base_path='/api/v1',
        options={"swagger_ui": True, "serve_spec": True},
        validate_responses=True
    )
    yield app


@pytest.fixture()
def client(connection_app):
    return connection_app.app.test_client()




