# config.py
from dotenv import load_dotenv
import os

load_dotenv()
api_url = os.getenv("API_URL")
print(api_url)  # Add this line