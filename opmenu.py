from system import systeminfo,systemping
from users import createUser, deleteUser
from stoRepo import listRepos, createRepo, updateRepo, storageInfo


def opmenu():
    while 1:
        print(" ")
        print(" ")
        print(" ")
        print("****Select an action****")
        print("1.Check state of Artifactory system")
        print("2.Get Artifactory system version")            
        print("3.Create new user")
        print("4.Delete existing user")
        print("5.Get storage informatoin")
        print("6.Create Repository")
        print("7.Update repository")
        print("8.List repositories")
        print("9.Exit")
        ac = input("Enter You choice: ")
        if ac == '1':
            systemping()
        elif ac == '2':
            systeminfo()
        elif ac == '3':
            createUser()
        elif ac == '4':
            deleteUser()
        elif ac == '5':
            storageInfo()
        elif ac == '6':
            createRepo()
        elif ac == '7':
            updateRepo()
        elif ac == '8':
            listRepos()
        elif ac == '9':
            break