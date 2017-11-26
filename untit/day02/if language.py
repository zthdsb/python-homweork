#if语法和if-elif-else的应用

import getpass #引用模块

_username='Adam'
_password='123'
username=input("username：")
password=input("password:")
#password=getpass.getpass("password:")
print(username,password)

if _username == username and _password ==password:
    print("Welcome user{name} login...".format(name=username))
else:
    print("Invalid username or password!")


age_of_oldboy=56
guess_age=int(input("guess age:"))
if guess_age == age_of_oldboy :
    print("yes,you get it!")
elif guess_age > age_of_oldboy:
    print("think smaller!")
else:
    print("think bigger!")