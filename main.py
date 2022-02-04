from autentication import login, signup
# Top menu
# to sign new user select 0
while 1:
    print("********** Artifactory Managment **********")
    print("1.Login")
    print("2.Exit")
    ch = input("Enter your choice: ")
    if ch == '0':
        signup()
    elif ch == '1':
        login()
    elif ch == '2':
        break
    else:
        print("Wrong Choice!")
