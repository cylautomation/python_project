import requests

response = requests.get("http://localhost:5000/")
print(response.status_code, response.json())