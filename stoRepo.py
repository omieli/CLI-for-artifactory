import json
import requests
from requests.structures import CaseInsensitiveDict
# set up headers for request
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiItZWt3X3V6Vk5yUlROOEh6MU5RbGh0VVZXbTV1ajExRnVSYmFPTkJnVFBNIn0.eyJleHQiOiJ7XCJyZXZvY2FibGVcIjpcInRydWVcIn0iLCJzdWIiOiJqZmFjQDAxZnRxOW5kcWVmOWNzMWFoOWY0NTcxazViXC91c2Vyc1wvb2hhZCIsInNjcCI6ImFwcGxpZWQtcGVybWlzc2lvbnNcL2FkbWluIiwiYXVkIjoiKkAqIiwiaXNzIjoiamZmZUAwMDAiLCJleHAiOjE2NzUzNTkwOTIsImlhdCI6MTY0MzgyMzA5MiwianRpIjoiMzg5MjRmOWEtOWNjOC00NmYzLTljODMtZTEzNDJmMWVlNTE5In0.OCqMxNFWoBIZFj3sE3S1KI2Ftcmdoc6cR9Bxq_gTbHMpR_u4XKGbKBgq4z0Oyhqp_DDUprQ_uQX7Hhj5qDr2UVFQjaSzAT9UHESGpvw_CROpprle-xGI5VvQTXLP20Ixkde0-j2-lwRLaIVQdvOB-lNN7a8KsKdeI-FtOt8z8ajMB6doGeUQmeLpgdj7UauRMYwUKPywiFi48VWlLh8tfNCZWtA2Fv6sRou7DTyIepATI9-kAUk6vRoZ7Flh9YgrS2ZtAsNuWYP5jNodNUIclegDtmY7ONJ-8UX8YOovCQ2mVxheiZRTTPkCfYU4tM6DU-5dUMKdfAHNhHOCCOWLCQ"
headers["Content-Type"] = "application/json"

# get storage information with GET request
# print the the output sorted and readable
def storageInfo():
    url = 'https://omieli.jfrog.io/artifactory/api/storageinfo'
    resp = requests.get(url, headers=headers)
    respSTR = json.loads(resp.text)
    print(json.dumps(respSTR,indent=4, sort_keys=True))

#create reposotory - error
def createRepo():
    repoKey = input('Enter repository key: ')
    rclass = input('Select class (local, remote, virtual or federated): ')
    url = 'https://omieli.jfrog.io/artifactory/api/repositories/'+repoKey
    data = {"key":repoKey,"rclass":rclass}
    resp = requests.put(url, headers=headers, json=data)
    if resp.status_code != 200:
        respSTR = json.loads(resp.text)
        print(respSTR["errors"])
    else:
        print(resp)

# request GET of all the repos availvable
def listRepos():
    url = 'https://omieli.jfrog.io/artifactory/api/repositories/'
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        respSTR = json.loads(resp.text)
        print(respSTR["errors"])
    else:
        print(resp.text)

#update reposotory - error
def updateRepo():
    listRepos()
    repoKey = input('Enter repository key: ')
    rclass = input('Select class (local, remote, virtual or federated): ')
    url = 'https://omieli.jfrog.io/artifactory/api/repositories/'+repoKey+'-H'
    data = {"key":repoKey,"rclass":rclass}
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code != 200:
        respSTR = json.loads(resp.text)
        print(respSTR["errors"])
    else:
        print(resp)


