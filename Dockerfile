FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y \
    gcc \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-k", "eventlet", "-c", "gunicorn_config.py", "app:app"]