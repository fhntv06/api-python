import requests

response = requests.get('https://google.com')


# print(response.headers)
# print(response.status_code)
# print(response.content)
print(response.text)