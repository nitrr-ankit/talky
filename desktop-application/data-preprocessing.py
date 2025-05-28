# Example code for rest API checks
# request module is simple way to make HTTP requests

import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(api_url)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error")
    print(errh.args[0])
else:
    print(f"Status Code is : {response.status_code}")

print(f"Response is : {response.json()}")