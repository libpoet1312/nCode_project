FROM python:3.6-alpine

COPY ./requirements.txt requirements.txt

WORKDIR .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["gunicorn", "--conf", "gunicorn_conf.py", "--bind", "0.0.0.0:5000", "app.api:app"]
