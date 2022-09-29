import functools
import sys
import os
import logging
from flask_caching import Cache
from config import BaseConfig
from flask import Flask, jsonify
from flask_restx import Api, Resource, reqparse

from consumer.consumer import Consumer

logging.basicConfig(level=logging.INFO)

# add this dir to Path so not to use relative imports
API_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(API_DIR))

app = Flask(__name__)

app.config.from_object(BaseConfig)
cache = Cache(app)

api = Api(app)


def make_response(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper', flush=True)
        result = func(*args, **kwargs)
        response = {
            'success': True,
            'result': result
        }
        status_code = 200
        return jsonify(response), status_code
    print('here')
    return wrapper


@cache.cached(timeout=30, query_string=True)
@api.route('/api/v1/stackstats')
class StackExchange(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('since')
        parser.add_argument('until')
        args = parser.parse_args()

        return Consumer().expose(args)


if __name__ == '__main__':
    app.logger.info("API running")
    app.run(debug=BaseConfig.DEBUG)
