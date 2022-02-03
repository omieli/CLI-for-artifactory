from ensurepip import version
import json
from os import system
import requests
from requests.structures import CaseInsensitiveDict

# set up headers for request
headers = CaseInsensitiveDict()
headers["Accept"] = "text/plain"
headers["Authorization"] = "Bearer eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiItZWt3X3V6Vk5yUlROOEh6MU5RbGh0VVZXbTV1ajExRnVSYmFPTkJnVFBNIn0.eyJleHQiOiJ7XCJyZXZvY2FibGVcIjpcInRydWVcIn0iLCJzdWIiOiJqZmFjQDAxZnRxOW5kcWVmOWNzMWFoOWY0NTcxazViXC91c2Vyc1wvb2hhZCIsInNjcCI6ImFwcGxpZWQtcGVybWlzc2lvbnNcL2FkbWluIiwiYXVkIjoiKkAqIiwiaXNzIjoiamZmZUAwMDAiLCJleHAiOjE2NzUzNTkwOTIsImlhdCI6MTY0MzgyMzA5MiwianRpIjoiMzg5MjRmOWEtOWNjOC00NmYzLTljODMtZTEzNDJmMWVlNTE5In0.OCqMxNFWoBIZFj3sE3S1KI2Ftcmdoc6cR9Bxq_gTbHMpR_u4XKGbKBgq4z0Oyhqp_DDUprQ_uQX7Hhj5qDr2UVFQjaSzAT9UHESGpvw_CROpprle-xGI5VvQTXLP20Ixkde0-j2-lwRLaIVQdvOB-lNN7a8KsKdeI-FtOt8z8ajMB6doGeUQmeLpgdj7UauRMYwUKPywiFi48VWlLh8tfNCZWtA2Fv6sRou7DTyIepATI9-kAUk6vRoZ7Flh9YgrS2ZtAsNuWYP5jNodNUIclegDtmY7ONJ-8UX8YOovCQ2mVxheiZRTTPkCfYU4tM6DU-5dUMKdfAHNhHOCCOWLCQ"

#check if Artifactory is working properly with GET request
def systemping():
    url = 'https://omieli.jfrog.io/artifactory/api/system/ping'
    headers["Content-Type"] = "text/plain"
    resp = requests.get(url, headers=headers)
    print("System status: "+resp.text)

#present artifactory system version
def systeminfo():
    url = 'https://omieli.jfrog.io/artifactory/api/system/version/'
    headers["Accept"] = "application/json"
    resp = requests.get(url, headers=headers)
    #load the json to a string
    respSTR = json.loads(resp.text)
    print(respSTR["version"])

    

