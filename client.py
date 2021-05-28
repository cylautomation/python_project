import requests

# response = requests.get("http://localhost:5000/")
# print(response.status_code, response.json())

response = requests.post("http://localhost:5000/", data={'cmd':'dir/w c:\\temp'})
print(response.status_code, response.json())
