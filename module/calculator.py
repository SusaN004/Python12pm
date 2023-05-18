
# def check_even_odd(n):
#     if n%2==0:
#         return "even"
    
#     else:
#         return "odd"




# with open("intro.txt", 'w') as obj:

# obj = open("intro.txt", 'a')
# obj.write("information of the student \n")
# name = input("Enter our name : ")
# email = input("Enter your email : ")
# address = input("Enter your address : ")
# phone = input("Enter your phone number : ")
# obj.write(f"your name is {name} email is {email} address is {address} and phone number is {phone}")
# obj.close()


# with open("students Marksheet.txt",'a') as obj:
#     obj.write("======= Students Marksheet========")
#     obj.write("\n")
#     name=input("Enter your name: ")
#     eng=int(input("Enter marks of english: "))
#     nep=int(input("Enter marks of Nepali: "))
#     mat=int(input("Enter marks of Maths: "))
#     sci=int(input("Enter marks of Science: "))
#     soc=int(input("Enter marks of Social: "))
#     obj.write("\n")
#     sum=nep+eng+mat+sci+soc
#     obj.write(f'Students id: {(name)} \n')
#     obj.write(f"The total marks of English is: {str(eng)} \n")
#     obj.write(f"The total marks of Nepali is: {str(nep)} ")
#     obj.write("\n")
#     obj.write(f"The total marks of maths is: {str(mat)} ")
#     obj.write("\n")
#     obj.write(f"The total marks of Science is: {str(sci)} ")
#     obj.write("\n")
#     obj.write(f"The total marks of Social is: {str(soc)} \n")
#     obj.write(f"The total marks is {str(sum)} \n")
#     percentage=sum/5
#     obj.write(f'The percentage is {str(percentage)}')


# with open ("intro.txt", 'r') as obj:
#     data = obj.readlines()
#     print(data)


    # def register():
    #     username = ''
    #     password = ''
    #     confirm_password = ''

    # def login():
    #     username = ''
    #     password = ''
    #     confirm_password = ''    



# import os

# if not os.path.exists('record.txt'):
#     open('record.txt', 'w').close()

# def register():
#     username = input('Enter username : ')
#     username = username.lower()
#     username = username.strip()
#     if username in open('record.txt', 'r').read():
#         print('username already exits')
#         exit()
#     password = input('Enter password: ')
#     password = password.strip()
#     confirm_password = input('Confirm password : ')
#     confirm_password = confirm_password.strip()
#     if password != confirm_password:
#         print('password does not match')
#         exit()
    
#     with open('record.txt', 'a') as f:
#         f.write(f'username : {username} password : {password}')
#         print('Registered sucessfully')

# def login():
#     print("===============login===============")
#     username = input('Enter username : ')
#     username = username.lower()
#     username = username.strip()
#     password = input('enter password : ')
#     password = password.strip()

#     with open('record.txt', 'r') as f:
#         find_users = []
#         for user in f.readlines():
#             find_users.append(user.split())
    
#     x = 0
#     total_user = len(find_users)
#     login_sucess = False
#     while x < total_user:
#         uname = find_users[x][0][9:]
#         upass = find_users[x][1][9:]
#         if uname == username and upass == password:
#             login_sucess = True
#         x +=1

#     if login_sucess:
#         print(f'Welcome{username}')
#     else:
#         print('username or password is incorrect')

# question = input('Do you have an account?(y/n):')
# question = question.lower()
# if question == 'y':
#     login()
# elif question== 'n':
#     register()
# else:
#     print('Invalid input')
#     exit()


