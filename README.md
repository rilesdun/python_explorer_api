# peerplays-explorer

![Pylint Badge](path_to_badge/pylint.svg)

Flask application for viewing information about the peerplays blockchain

Install dependencies:

- `pip install -r requirements.txt`

Run in development mode:

- `python3 app.py run`

Run in production mode:

- `gunicorn -k eventlet -w 1 -c gunicorn_config.py app:app`
