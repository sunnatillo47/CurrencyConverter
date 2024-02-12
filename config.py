import json
import requests

TOKEN = '6144862113:AAGYuQAPe_s4akcwENpe_7gCAHU3lzQc_gQ'

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
response = requests.get(url)
course = response.json()