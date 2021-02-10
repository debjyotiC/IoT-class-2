import requests
import json

# url = 'https://api.thingspeak.com/channels/1268329/feeds.json?api_key=WQE3YER1L6F7F8HK&results=2'
url = 'http://192.168.0.107:5000/feeds.json?api_key=KDT6QF1NGR35KXKL0Q-DOG'
response = json.loads(requests.get(url).content)

print(response)