# nCode_project

This is a project aiming to show my abilities to develop a consumer application written in Python for the StackExchange API.

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker-compose](https://docs.docker.com/compose/install/)

## Architecture

This is an api written in Python with Flask framework that consumes StackExchange API
and provides an endpoint in which some calculations/statistics are provided.

Endpoints:
- api/v1/stackstats : The requested endpoint for our calculations,

### Based on

- Python: 3.6.15
- Flask: 2.0.3

### 3rd party Python Libraries used

- [Flask-RESTX](https://flask-restx.readthedocs.io)
- Flask-Caching
- Redis

## Folder structure

    | nCodeProject/ : Root application folder
    | -- app/ : Entrypoint application folder
    | ---- main.py : Entrypoint
    | ---- config.py : Store config variables
    | ---- consumer/ : A module that makes all calculations and API requests to StackExchange API
    | ------ consumer.py
    | ------ helpers.py
    | -- docker-compose.yml : for production use
    | -- docker-compose-dev.yml : for dev use
    | -- .env
    | -- .env_back
    | -- Dockerfile.dev
    | -- Dockerfile
    | -- requirements.txt : Python libraries required
    | -- gunicorn_conf.py : Gunicorn conf file, for production use

## Development
Firstly we need to copy .env_back to .env
```shell
cp .env_back .env
```

### 1. With docker

```shell
docker-compose -f docker-compose.yaml up -d --build
```

### 2. Without docker
To run for development (without cache support) run:
```shell
python main.py
```

## Deployment

For presentation, we use docker and docker-compose.

0. Copy _.env_ from _.env_back_
    ```shell
    cp .env_back .env
    ```
1. Build docker containers
    ```shell
    docker-compose -f docker-compose.yaml up -d --build
    ```
2. Example:
   ```shell
   curl --request --url http://127.0.0.1:5000/api/v1/stackstats?since=2020-10-02%2010:00:00&until=2020-10-02%2011:00:00
   ```

## Testing

We use pytest for testing our code/api.
We have included 5 basic tests in order to do so.

Run:
```shell
python -m pytest
```

