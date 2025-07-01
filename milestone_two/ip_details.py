import requests
url = 'https://api.ipify.org?format=json'
r = requests.get(url)
ip = r.json().get('ip')
print(ip)
detail_url = f'https://ip-api.com/json/{ip}'
response = requests.get(detail_url)
print(response.json())