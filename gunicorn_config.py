"""
Gunicorn config file
"""

import multiprocessing

bind = "0.0.0.0:5000"  # pylint: disable=invalid-name
worker_class = 'eventlet' # pylint: disable=invalid-name
workers = multiprocessing.cpu_count() * 2 + 1
