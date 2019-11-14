import requests
from requests.auth import HTTPBasicAuth

url='https://digital.vfc.com/jira/secure/Dashboard.jspa'
headers = { "Accept" : "application/json",
            "Authorization" : "Basic a3Jpc2huYS5zaW5naDE2QHdpcHJvLmNvbTozOTY1NzU="}
# response = requests.request(method='GET', url=url)
# a3Jpc2huYS5zaW5naDE2QHdpcHJvLmNvbTozOTY1NzU=

response = requests.get(url=url, headers=headers)
print(response.text)

