import connexion
from flask_caching import Cache

from app.consumer.consumer import Consumer
from app.config import BaseConfig

app = connexion.FlaskApp(__name__, specification_dir='')

flaskApp = app.app
flaskApp.config.from_object(BaseConfig)
cache = Cache(flaskApp)


@cache.cached(timeout=30, query_string=True)
def index(since, until=None):
    return Consumer().expose(since, until)


if __name__ == '__main__':
    app.add_api(
        'nCode_openapi3.0.yaml',
        base_path='/api/v1',
        options={"swagger_ui": True, "serve_spec": True},
        validate_responses=True
    )
    app.run(debug=True)
