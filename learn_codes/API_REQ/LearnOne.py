import requests
from requests import Response

url = 'https://www.google.co.in/search?q=God'
headers = {}
payload = {}
response = requests.request('GET', url,  data = payload, headers = headers, allow_redirects=False, timeout=10)
a = response.headers

for k, v in a.items() :
    print(k, ':', v, '\n')

resp: Response = requests.get(url="https://reqres.in/api/users?page=2")
print("Hi This Is Response Content :: \n", resp.content)
print("Hi This Is Status Code :: ", resp.status_code)