import requests

url = "https://httpbin.org/get"

response = requests.get(url)

print("Status:", response.status_code)
print("Response:", response.json())