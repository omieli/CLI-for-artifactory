import json
import requests
from requests.structures import CaseInsensitiveDict

# set up headers for request
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiItZWt3X3V6Vk5yUlROOEh6MU5RbGh0VVZXbTV1ajExRnVSYmFPTkJnVFBNIn0.eyJleHQiOiJ7XCJyZXZvY2FibGVcIjpcInRydWVcIn0iLCJzdWIiOiJqZmFjQDAxZnRxOW5kcWVmOWNzMWFoOWY0NTcxazViXC91c2Vyc1wvb2hhZCIsInNjcCI6ImFwcGxpZWQtcGVybWlzc2lvbnNcL2FkbWluIiwiYXVkIjoiKkAqIiwiaXNzIjoiamZmZUAwMDAiLCJleHAiOjE2NzUzNTkwOTIsImlhdCI6MTY0MzgyMzA5MiwianRpIjoiMzg5MjRmOWEtOWNjOC00NmYzLTljODMtZTEzNDJmMWVlNTE5In0.OCqMxNFWoBIZFj3sE3S1KI2Ftcmdoc6cR9Bxq_gTbHMpR_u4XKGbKBgq4z0Oyhqp_DDUprQ_uQX7Hhj5qDr2UVFQjaSzAT9UHESGpvw_CROpprle-xGI5VvQTXLP20Ixkde0-j2-lwRLaIVQdvOB-lNN7a8KsKdeI-FtOt8z8ajMB6doGeUQmeLpgdj7UauRMYwUKPywiFi48VWlLh8tfNCZWtA2Fv6sRou7DTyIepATI9-kAUk6vRoZ7Flh9YgrS2ZtAsNuWYP5jNodNUIclegDtmY7ONJ-8UX8YOovCQ2mVxheiZRTTPkCfYU4tM6DU-5dUMKdfAHNhHOCCOWLCQ"
headers["Content-Type"] = "application/json"

#create new user with PUT request
def createUser():
    username = input('Select user name: ')
    email = input('Enter your email: ')
    password = input('Select password: ')
    url = 'https://omieli.jfrog.io/artifactory/api/security/users/'+username
    data = {"email":email,"password":password}
    resp = requests.put(url, headers=headers, json=data)
#check if request succed
    if resp.status_code != 201:
        respSTR = json.loads(resp)
        print(respSTR["errors"])
    else:
        print("User created successfully")

#present all users available with GET request and enter the name to DELETE request
def deleteUser():
    url = 'https://omieli.jfrog.io/artifactory/api/security/users'
    allusers = requests.get(url, headers=headers)
    print("****Available Users****")
    allusersSTR = json.loads(allusers.text)
    for user in allusersSTR:
        print(user["name"])
    usertoDelete = input("Select user from the list above for delete: ")
    url = 'https://omieli.jfrog.io/artifactory/api/security/users/'+usertoDelete
    resp = requests.delete(url, headers=headers)
    print(resp.text)






