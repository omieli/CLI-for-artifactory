from opcode import opname
from opmenu import opmenu

#login and sign up functions
#the user name and password will be stored in credentials.txt



def signup():
    db = open("credentials.txt","r")
    usrname = input("Enter user name: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
#edit user name and password before add to .txt
    d = []
    f = []
    for i in db:
        a,b = i.split(",")
        d.append(a)
        f.append(b)
#check if password confirmed
    if pwd != conf_pwd:
        print("Password don't match")
        signup()
    else:
#check for duplicate user name
        if usrname in db:
            print("User name exist")
            signup()
        else:
#add credentials to .txt
            db = open("credentials.txt","a")
            db.write(usrname+","+pwd+"\n")
            print("You have registered successfully!")
            
    
def login():
    db = open("credentials.txt","r")
    usrname = input("Enter user name: ")
    pwd = input("Enter password: ")
#check if password or username inserted
    if not len(usrname or pwd)<1:
#edit user name and password before add to .txt
        d=[]
        f=[]
        for i in db:
            a,b = i.split(",")
            b=b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d,f))
#check if user name exist
        if data[usrname]:
            if pwd == data[usrname]:
                print("Login successfully")
                opmenu()
            else:
                print("Password or username incorrect")
        else:
            print("Username doesn't exist")
    else:
        print("Please enter a value")
