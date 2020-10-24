import requests
import json

response = requests.get("https://api.themoviedb.org/3/movie/?api_key=1ed81738f71756c66a2146addd890cfc")
response = response.json()
print(response)