import requests

url = 'http://127.0.0.1:8000/service/create/'

response = requests.patch(url, json={ 'title': 'new 1', 'position': 'tel aviv', 'description':' super'} )
print(response.json())
print(response.status_code)