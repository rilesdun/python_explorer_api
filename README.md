# peerplays-explorer

Flask application for viewing information about the peerplays blockchain

Install dependencies:

- `pip install -r requirements.txt`

Run in development mode:

- `python3 app.py run`

Run in production mode:

- `gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -c gunicorn_config.py app:app`