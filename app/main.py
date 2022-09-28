import connexion
import logging
from flask_caching import Cache
from config import BaseConfig

from consumer.consumer import Consumer

logging.basicConfig(level=logging.INFO)

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
    )
    flaskApp.logger.info("API running")
    app.run(debug=BaseConfig.DEBUG)
