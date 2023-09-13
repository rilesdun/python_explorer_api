#bind = "0.0.0.0:5000" 
#workers = 4 

# gunicorn_config.py
import multiprocessing

bind = "0.0.0.0:5000"
worker_class = 'eventlet'
workers = multiprocessing.cpu_count() * 2 + 1