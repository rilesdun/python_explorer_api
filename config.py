"""
Function for loading .env files
"""

import os
from dotenv import load_dotenv

load_dotenv()
api_url = os.getenv("API_URL")
print(api_url)
