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

    | app/
    |-- consumer/
    |---- consumer.py
    |---- helpers.py
    |-- config.py
    | docker-compose.yml
    | .env
    | Dockerfile
    | main.py
    | nCode_openapi3.0.yaml
    | requirements.txt

## Presentation

For presentation, we use docker and docker-compose.

``` 
docker-compose -f docker-compose.yaml up -d --build
```
