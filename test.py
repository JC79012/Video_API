import requests

# location of the API
BASE="http://127.0.0.1:5000/"

# tests to be placed here 


response = requests.get(BASE + "video/6")
print(response.json())
