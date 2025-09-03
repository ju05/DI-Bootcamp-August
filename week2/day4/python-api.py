import requests
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "jokes.json")


jokes = []
for _ in range(10):
    response = requests.get('https://api.chucknorris.io/jokes/random')

    # print(response) it will print a response code

    data = response.json()

    # print(data['joke']) #this crashs the code
    jokes.append(data)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(jokes, f, indent=2, sort_keys=True)

print('json file sucessfull created')

