import requests
import json

url = 'https://api.thingspeak.com/update?api_key=YMG26ZD34A06YMMT&'  # request URL
update = {'field1': 100}  # payload

response = requests.get(url, data=update)

print(response)
