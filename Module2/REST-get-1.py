import requests
import json

# url = 'https://api.thingspeak.com/update?api_key=YMG26ZD34A06YMMT&'  # request URL
url = 'http://192.168.0.107:5000/update?api_key=KDT6QF1NGR35KXKL0Q-DOG&'
update = {'field1': 21.3}  # payload

response = requests.get(url, data=update)

print(response)
