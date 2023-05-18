
import os
if not os.path.exists('document.txt'):
    open('document.txt','w').close()

def register():
    print("=============Register================")

username = input('enter user : ')
username = username.lower()
username = username.split()
if username in open('record.txt', 'r'):
    print('Username already exits')
    exit()

password = input('Enter password : ')
password = password.split()
confirm_password = input('Confirm password : ')
confirm_password = confirm_password.split()

if password != confirm_password:
    print('Password doesnot match')
    exit()

with open('document.txt', 'a') as f:
    f.write(f'username : {username} password : {password}\n')
    print('Registered sucessfully')

def login():
    print("==============login================")
    username = input('Enter username: ')
    username = username.lower()
    username = username.split()
    password = input('Enter password: ')
    password = password.split()

    with open('document.txt', 'r') as f :
        find_users = []
        for user in f.readlines():
            find_users.append(user.split())

    x = 0
    total_users = len(find_users)
    login_sucess = False
    while x < total_users:
        uname = find_users[x][0][9]
        upass = find_users[x][1][9]
        if uname == username and upass == password :
            login_sucess = True

        x += 1
    
    if login_sucess:
        print(f'Welcome {username}')
    else:
        print('Username or Password incorrect')

question = input('Do you have an account?(y/n): ')
question = question.lower()
if question == 'y':
    login()
elif question == 'n' :
    register()
else:
    print('Invalid input')

    exit()



    