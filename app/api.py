import functools
import sys
import os
import logging
from flask_caching import Cache
from config import BaseConfig
from flask import Flask
from flask_restx import Api, Resource, reqparse

from consumer.consumer import Consumer

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app.config.from_object(BaseConfig)
cache = Cache(app)

api = Api(app)


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
