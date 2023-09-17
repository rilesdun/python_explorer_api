"""
Cache configuration for the application.
"""
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'simple'})
