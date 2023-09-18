# Peerplays Explorer

Peerplays Explorer is a Flask application for viewing information about the Peerplays blockchain. It provides various endpoints to fetch data like account information, supply details, latest transactions, and more.

## Features

- Fetch account information
- Get supply details for various assets
- Retrieve latest transactions (requires improvements, PRs welcome)
- View active witnesses and sons
- Get account history
- Fetch rich list for a given coin

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

- Run in development mode:
  
```bash

python3 app.py run
```

- Run in production mode:

```bash
gunicorn -k eventlet -w 1 -c gunicorn_config.py app:app
```


## Docker

You can also run the application using Docker. Build the Docker image and run it:

```bash
docker build -t peerplays-explorer .
docker run -p 5000:5000 peerplays-explorer
```
