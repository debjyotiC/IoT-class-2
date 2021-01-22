import requests
import json

url = 'https://api.thingspeak.com/channels/1268329/feeds.json?api_key=WQE3YER1L6F7F8HK&results=2'

response = json.loads(requests.get(url).content)

print(response['feeds'])