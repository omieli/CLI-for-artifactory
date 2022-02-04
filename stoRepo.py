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
    print(json.dumps(respSTR, indent=4, sort_keys=True))

# create reposotory with PUT request
# create repo type:"remote" still have errors


def createRepo():
    repoKey = input('Enter repository key: ')
    rclass = input('Select class (local, remote, virtual or federated): ')
    print('maven|gradle|ivy|sbt|helm|cargo |cocoapods|opkg|rpm|nuget|cran|gems|npm|bower|debian|composer|pypi|docker|vagrant|gitlfs|go|yum|conan|chef|pub|puppet|generic')
    packType = input('Select package type from the list above: ')
    if rclass == "remote":
        repoURL = input("Enter reposetory URL: ")
        data = {"key": repoKey, "rclass": rclass,
                "packageType": "docker", "url": repoURL}
    else:
        data = {"key": repoKey, "rclass": rclass, "packageType": "docker"}
    url = 'https://omieli.jfrog.io/artifactory/api/repositories/'+repoKey
    headers["Accept"] = "text/plain"
    resp = requests.put(url, headers=headers, json=data)
    print(resp.text)

# request GET of all the repos availvable


def listRepos():
    url = 'https://omieli.jfrog.io/artifactory/api/repositories'
    headers["Accept"] = "application/json"
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        respSTR = json.loads(resp.text)
        print(respSTR["errors"])
    else:
        print(resp.text)
