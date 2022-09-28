import sys
import os
import connexion
import logging
from flask_caching import Cache
from config import BaseConfig

from consumer.consumer import Consumer

logging.basicConfig(level=logging.INFO)

# add this dir to Path so not to use relative imports
API_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(API_DIR))

app = connexion.FlaskApp(__name__, specification_dir='')

flaskApp = app.app
flaskApp.config.from_object(BaseConfig)
cache = Cache(flaskApp)


# @cache.cached(timeout=30, query_string=True)
def index(since, until=None):
    return Consumer().expose(since, until)


app.add_api(
    'nCode_openapi3.0.yaml',
    base_path='/api/v1',
    options={"swagger_ui": True, "serve_spec": True},
)

if __name__ == '__main__':
    flaskApp.logger.info("API running")
    app.run(debug=BaseConfig.DEBUG)
