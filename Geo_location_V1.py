import requests
import json

#ip adress
ip_address = '147.229.2.90'

#IP address
request_url = 'https://geolocation-db.com/jsonp/' + ip_address

#send request and decode the result
response = requests.get(request_url)
result = response.content.decode()
#clean the returned string 
result = result.split("(")[1].strip(")")

#convert
result = json.loads(result)
print(result)
