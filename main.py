import connexion

from app.consumer.consumer import Consumer

app = connexion.FlaskApp(__name__, specification_dir='')

def index(since, until=None):
    return Consumer().expose(since, until)


if __name__ == '__main__':
    app.add_api(
        'nCode_openapi3.0.yaml',
        base_path='/api/v1',
        options={"swagger_ui": True, "serve_spec": True},
        validate_responses=True
    )
    app.run(host='127.0.0.1', debug=True)