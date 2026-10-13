import requests

url = "https://httpbin.org/post"

data = {
    "name": "Shloka",
    "role": "Intern"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)