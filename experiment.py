import requests

url = "https://youtest.me/find?id=cg8t1oY&q=1"
response = requests.get(url)
print(response.text)  # Check for answer in the response
