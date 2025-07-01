# Sources:
    # keyword: python request module
    # site: https://pypi.org/project/requests/
    # ipify: https://www.ipify.org/
    # HTML request code

import requests
url = 'https://api.ipify.org?format=json'
response = requests.get(url)
# print(response.json())
data = response.json()
ip = data ['ip']
print(f'Your IP address is {ip}')
