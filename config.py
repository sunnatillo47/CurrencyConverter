import json
import requests

TOKEN = '6144862113:'

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
response = requests.get(url)
course = response.json()