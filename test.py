import requests
import json
URL = "http://localhost:8000/api/movies/"

for i in range(1, 8):
    if i != 5:
        r1 = requests.get(URL + str(i))
        r1 = r1.json()
        print(r1)