# nCode_project

This is a project aiming to show my abilities to develop a consumer application written in Python for the StackExchange API.

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker-compose](https://docs.docker.com/compose/install/)

## Architecture

This is an api written in Python with Flask framework that consumes StackExchange API
and provides an endpoint in which some calculations/statistics are provided.

### Based on

- Python: 3.6.15
- Flask: 2.0.3

### 3rd party Python Libraries used

- [connection](https://connexion.readthedocs.io/en/latest/)
- Flask-Caching
- Redis

## Folder structure

    | nCodeProject/ : Root application folder
    | -- app/ : Entrypoint application folder
    | ---- main.py : Entrypoint
    | ---- config.py : Store config variables
    | ---- nCode_openapi3.0.yaml : An open3.0 spec file that describes the API
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

0.
    ```shell
    cp .env_back .env
    ```
1.
    ```shell
    docker-compose -f docker-compose.yaml up -d --build
    ```


