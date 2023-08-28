import requests

url = f'http://openapi.clearspending.ru/restapi/v3/contracts/search/'
data = requests.get(url)
print(data)