import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "http://127.0.0.1:8000/generate?prompt=Tell me about the car industry in Mexico"
headers = {"x-api-key": os.getenv("API_KEY"), "Content-Type": "application/json"}

response = requests.post(url, headers=headers)
print(response.json())