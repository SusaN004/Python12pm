# print("Hello")
# print(2345)
# print("My name is Susan Poudel")
# print("My address is Bharatpur")
# print(9845150596)
# print("City is Chitwan")
# name = "susan poudel"
# email  = "gec.susan2022@gmail.com"
# address = "Chitwan"
# phone = 9845150596
# print(name)
# a = 5
# b = 10
# c = a+b
# print(c)
# d = ("p")
# print(f"my name is {name}")


# print(type(x))
# x=9845150596
# print(dir(x))
# a=input("enter name: ")
# b=input("enter address: ")
# c=input("enter phone: ")
# d=input("enter email: ")
# print(a,b,c,d)
# x =int(input("enter x: "))
# y =int(input("enter y: "))
# print(x+y)
# name = "susan"
# age = 29
# print(f"name is {name} age is {age}")
# name, age = input("Enter name and age example name,age:").split(",")
# print(f"my name is {name} and age is {age}")

# x='10'
# print(type(x))
# x= int(x)
# print(type(x))
# x = int(input("Enter x: "))
# y = input("enter y: ")
# y = int(y)
# print(x+y)

# data = [
#     ['ram', 'sita', 'gita'],
#     ['hari', 'shyam', 'mohan'],
#     ['suresh', 'ghanshyam', 'mahesh']
# ]
# print(data[2][0])

# data = [
#     ['ram', 'sita', 'gita'],
#      ['hari', 'shyam', 'mohan'],
#      ['suresh', 'ramesh', 'mahesh'],
#      ['sophia',[[[['python']]]],'sara']
# ]
# print(data[3][1][0][0][0][0])

# data = ['ram', 'sita']
# data[0] = ['hari']
# print (data)
# data = 'ram'
# print(dir(data))

# data[]
# data.append('ram')
# print(data)

# data = ['ram', 'sita', 'sita']
# print(data.count('sita'))

# data = ['ram', 'sita']
# data1 = ['hari', 'gita']
# data.extend(data1)
# print(data)

# course = "python for beginners"
# print(course.upper())

# course = "PYTHON FOR BEGINNERS"
# print(course.lower())

# course = "python for beginners"
# print(course.title())

# course = "python for beginners"
# print(course.find("for"))
# course = "python for beginners"

# print (course.replace("beginners", "absolute beginners"))

# course = "python for beginners"
# print("python" in course)

# print("mother's")
# print('mother\'s')

# print("\"mother\"")
# print('\'mother\'')
# print('mother\'s')

# course = """
# we are learning python
# for beginners
# """
# print(course)

# x = 5
# y = 10
# z = 30
# b = 10
# sum = x + y + z + b
# print(f"total sum is = {sum}")

# process = f"""
# x = {x}
# y = {y}
# z = {z}
# b = {b}
# _________
# Sum = {sum}
# """
# print(process)

# name = input("enter name:")
# age = input("enter age:")
# phone = input("enter phone number:")
# print(f"my name is {name} my age is {age} and phone number is {phone}")

# fName = input("Enter frist name: ")
# lName = input("Enter last name: ")
# fullName = fName + " " + lName
# print(f"My name is {fullName.title()}.")

# a = 5
# a +=60
# print(a)

# a = 5
# b = 10
# c = a
# print(a is b)
# print(a is c)
# print(a is not b)

# nepali = int(input("Enter obtained marks of nepali : "))
# english = int(input("Enter obtained marks english : "))
# math = int(input("Enter obtained marks of math : "))
# science = int(input("Enter obtained marks of science :"))
# social = int(input("Enter obtained marks of social :"))
# total = nepali + english + math + science + social
# percentage = total/5
# print(total)
# print (percentage)

# data = {'sita', 'ram', 'gopal'}
# data = list(data)
# if 'gopal' in data:
# print('gopal')

# data = {'name': 'ram', 'age' : 20}
# print(data['name'])

# users = {
#     'name': 'hari',
#     'address': {
#     'city': 'kathmandu',
#     }
# }
# print(users['address']['city'])

# students = [
#     {
#     'name': 'ram',
#     'age': 20,
#     },
#     {
#     'name': 'ram',
#     'age': 21,
#     }
# ]
# print(students[0]['name'])

# user = []
# name = input('Enter a name : ')
# email = input('Enter a email : ')
# phone = input('Enter a phone number : ')
# user.append(name)
# user.append(email)
# user.append(phone)
# print(user)

# x = int(input('Enter the value :'))
# y = int(input('Enter the value :'))
# z = int(input('Enter the value :'))
# data = [x, y, z]
# data.sort(reverse=True)
# print(data)

# data = ['ram', 'shyam', 'hari', 'gita']
# extra = input('enter a name : ')
# data.insert(2, extra)
# print(data)

# a = int(input("enter a number : "))
# b = int(input("enter a number : "))
# if a>b:
#    print(f"{a} is greater than {b}")
# else:
#    print(f"{a} is smaller than {b}")

# age = int(input("Enter your age : "))
# if age<18:
#     print("you cannot vote")
# elif age < 40:
#     print("you can vote")
# else:
#     print("You cannot vote")

# number = int(input("Enter a number :"))
# if number % 2==0:
#     print("number is even")
# else:
#     print("number is odd")

# number = int(input("enter a number :"))
# if number % 3==0 and number % 5==0 :
#     print("number is divisible by both")
# else:
#     print("number is not divisible by 3 and 5")

# nepali = int(input("enter mark of nepali :"))
# english = int(input("enter mark of english :"))
# maths = int(input("enter mark of maths :"))
# science = int(input("enter mark of science :"))
# social = int(input("enter mark of social :"))
# total = nepali + english + maths + science + social
# percentage = total/5
# if percentage<35:
#     print("fail")
# elif percentage > 35 and percentage < 45:
#     print("you passed with grade C")
# elif percentage<=55:
#     print("you passed with grade B")
# elif percentage<=65:
#     print("you passed with grade A")
# elif percentage<=75 :
#     print("you passed with A+")
# else:
#     print("you passed with A++")

# username = input("Enter user name : ")
# password = input("Enter a password : ")
# if username == "admin" and password == "admin002" :
#     print("welcome")
# elif username == "ram" and password == "ram002":
#     print("welcome ram")
# else:
#     print("your username or password is incorrect")

# users=[
#     {"username":"admin", "password" : 'admin002'},
#     {"username":"ram", "password":"ram002"}
# ]
# user = input("enter a username : ")
# password = input("enter a password :")
# users=list(users)
# if user == 'admin' and password == 'admin002' or user =='ram' and password == 'ram002':
#     print(f"you are welcome {user}")
# else:
#     print("username or password is imcorrect")

# x = 25
# y = 20
# z = 30
# if x > y :
#     if x > z :
#         print("x is greater than y and z")
#     else:
#         print("z is greater than x and y")
# else:
#     if y>z:
#         print("y is greater than x and z")
#     else:
#         print("z is greater than x and y")


# username = input("enter the username: ")
# password = input("enter the password: ")
# if username =="admin" or username =="ram":
#     print("user name is correct")
# else:
#    print("user name incorrect")

# if password=="admin002" or password=="ram002":
#     print("welcome to the app")
# else:
#     print("password is incorrect")

# a = int(input("if you want addition type 1"))
# b = int(input("if you want subtraction type 2"))
# c = int(input("if you want multiplication type 3"))
# d = int(input("if you want division type 4"))
# if a ==1:
#  x=int(input("enter a value x : "))
#  y=int(input("enter the value of y : "))
# total = x + y
# print("total")
# if b==2 :
#   x=int(input("enter a value x : "))
#   y=int(input("enter the value of y : "))
# total = x - y
# print("total")
# if c==3 :
#    x=int(input("enter a value x : "))
#    y=int(input("enter the value of y : "))
# total = x * y
# print("total")

# if d == 4 :
#  x=int(input("enter a value x : "))
#  y=int(input("enter the value of y : "))
#  total = x / y
# print("total")

# print("1. addition 2. subtraction 3. multiplication 4. division")
# option = int(input("Enter option:"))
# if option ==1:
#     x = int(input("Enter x : "))
#     y = int(input("Enter y : "))
#     print(f"Addition of {x} and {y} is {x+y}")
# elif option ==2 :
#     x = int(input("Enter x : "))
#     y = int(input("Enter y : "))
#     print(f"subtraction of {x} and {y} is {x - y}")


# print("==================Computer Bazar=====================")
# print("1. Dell(Rs:20000) 2. Toshiba(Rs:30000) 3. MAC(Rs.50000)")
# option = int(input("Enter your option: "))
# product_name = ""
# dell_price = 0
# toshiba_price = 0
# mac_price = 0
# quantity = 0
# delivery_charge = 0
# plastic_bag = 0
# bag_price = 0
# gift_box_price = 0
# tax_amount = 0

# if option == 1:
#     quantity = int(input("Enter quantity: "))
#     product_name = "Dell"
#     dell_price = quantity * 20000
# elif option == 2:
#     quantity = int(input("Enter quantity: "))
#     product_name = "Toshiba"
#     toshiba_price = quantity * 30000
# elif option == 3:
#     quantity = int(input("Enter quantity: "))
#     product_name = "Mac"
#     mac_price = quantity * 50000
# else:
#     print("Invalid option")
#     exit()
# print("Delivery Options: 1. Home Delivery(Rs:1000) 2. Pick up(Rs.0)")
# delivery_option = int(input("Enter your option: "))
# if delivery_option ==1:
#     delivery_charge=1000
# print("1. Plastic Bag : (500) 2. Bag:(2000) 3. Gift Box(5000) 4. None")
# bag_option = int(input("Enter your option : "))
# if bag_option==1:
#     plastic_bag = 500
# elif bag_option ==2:
#     bag_price = 2000
# elif bag_option ==3:
#     gift_box_price = 5000
# else:
#     print("Invalid option")

# total = dell_price + toshiba_price + mac_price
# print("Location : 1. Kathmandu(Rs:13% tax) 2. Lalitpur 3. Bhaktapur")
# location = int(input("Enter your option: "))
# if location ==1:
#     tax_amount = total * 0.13

# grand_total = total + delivery_charge + plastic_bag + bag_price + gift_box_price + tax_amount
# print("==========Bill==========")
# print("Product Name:", product_name)
# print("Quantity:", quantity)
# print("Delivery Charge:, delivery_charge")
# print("Plastic Bag:", plastic_bag)
# print("Bag:", bag_price)
# print("Gift Box:", gift_box_price)
# print("Tax Amount:", tax_amount)
# print("Grand Total:", grand_total)


# print("1.NTC to NTC")
# print("2.NTC to NCELL")
# print("3. NCELL to NTC")
# print("4. NCELL to NCELL")
# option = int(input("Enter your option: "))
# if option == 1:
#     duration = int(input("Enter duration: "))
#     if duration > 100:
#         print("Invalid duration")
#         exit()
#     if duration <= 10:
#         bonus = 2.5
#         print("Bonus: ", bonus)
#     elif duration <= 20:
#         bonus = 5
#         print("Bonus: ", bonus)
#     elif duration <= 30:
#         bonus = 7.5
#         print("Bonus: ", bonus)
#     elif duration <= 40:
#         bonus = 10
#         print("Bonus: ", bonus)
#     elif duration <= 50:
#         bonus = 12.5
#         print("Bonus: ", bonus)
#     elif duration <= 60:
#         bonus = 15
#         print("Bonus: ", bonus)
#     elif duration <= 70:
#         bonus = 17.5
#         print("Bonus: ", bonus)
#     elif duration <= 80:
#         bonus = 20
#         print("Bonus: ", bonus)
#     elif duration <= 90:
#         bonus = 22.5
#         print("Bonus: ", bonus)
#     elif duration <= 100:
#         bonus = 25
#         print("Bonus: ", bonus)

# data = ['ram', 'shyam', 'hari', 'gita']
# for name in data:
#     print(name)


# numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
# for odd_even in numbers:
#     if odd_even % 2 == 0 :
#         print(odd_even, " is even number")
#     else:
#         print(odd_even, " is odd number")

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
# even = 0
# odd = 0
# for n in numbers:
#     if n % 2 == 0 :
#         even = even + 1
#     else:
#         odd = odd + 1
# print("even = ", even)
# print("odd: ", odd)


# data = ['ram', 'shyam', 'hari', 'gita', 'ram', 'ram', 'gita']
# ram = 0
# gita = 0
# for name in data :
#     if name == 'ram':
#         ram += 1
#     elif name == 'gita':
#         gita += 1
# print(f"Number of name ram is : {ram}")
# print(f"Number of name gita : {gita}")

# data = [
#     ['ram','shyam', 'hari', 'gita']
#     ['sophia', 'sara', 'susan', 'sophie']
#     ['jhon', 'james', 'jim','joe']
# ]
# for user in data:
#     for name in user:
#         print(name)

# num = int(input("Enter a number : "))
# names = []
# for i in range(num):
#     name = input("Enter a name : ")
#     names.append(name)
# for n in names :
#     print(n)

# num = int(input("Enter a number : "))
# number = []
# for i in range(num):
#     number = input("Enter a number : ")
#     number.append.(number)
#     number.count
# for n in number :
#     print(n)

# while loop 

# x = 1
# while x<=10:
#     print(x)
    # x +=1

# x = 1
# total_even = 0
# total_odd = 0
# while x <= 10:

#     if x % 2 == 0 :
#         total_even =+ 1
#     else:
#         total_odd =+ 1
# print(f"Total even numbers: {total_even}")
# print(f"Total odd numbers: {total_odd}")

# users = ['ram', 'sita', 'ram', 'ram']
# for user in users:
#     if user =='ram':
#         print(user)

# users = ['ram', 'sita', 'ram', 'ram']
# x=0

# while x<len(users):
#     if users[x] == 'ram':
#         print(users[x])
#     x+=1

# number = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# for num in number:
#     if num % 2 == 0 :
#         print(num)



# number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# x = 0
# while x<len(number):
#     if number[x] % 2 == 0:
#         print(number[x])    
#     x+=1

# num_time = int(input("Enter a number: "))
# increment=1
# rep_number = []
# list_of_number = []

# while increment<=num_time:
#     number = int(input("Enter a number: "))
#     if not number in rep_number:
#         rep_number.append(number)
#     else:
#         list_of_number.append(number)

#     increment +=1
# print(rep_number)

# for i in range(11):
#     print("2 X",i,"=",2*i)
# for i in range(11):
#     print("3 X",i,"=",3*i) = 1

# for i in range(11):
#     print("4 X",i,"=",4*i)
# for i in range(11):
#     print("5 X",i,"=",5*i)
# for i in range(11):
#     print("6 X",i,"=",6*i)
# for i in range(11):
#     print("7 X",i,"=",7*i)
# for i in range(11):
#     print("8 X",i,"=",8*i)
# for i in range(11):
#     print("9 X",i,"=",9*i)
# for i in range(11):
#     print("10 X",i,"=",10*i)

    
# number=int(input("Enter the number which you want multiplication : "))



# num_of_students = int(input("Enter a number of students: "))
# increment = 1
# total_marks = []

# while increment <= num_of_students:
#     print(f"===========Student Id: {increment}==========")
#     for i in range(1):
#         nepali = int(input("Enter a mark of nepali: "))
#         english = int(input("Enter a mark of english: "))
#         math = int(input("Enter a mark of math: "))
#         social = int(input("Enter a mark of social: "))
#         science = int(input("Enter a mark of science: "))
#         total = nepali + english + math + social + science
#         total_marks.append(total)
#     increment +=1

# sId = 1
# for mark in total_marks:
#     total = mark
#     percentage = mark / 5
#     grade = ''
#     if percentage >= 80:
#         grade = 'A'
#     elif percentage >= 70:
#         grade = 'B'
#     elif percentage >= 60:
#         grade = 'C'
#     elif percentage >= 50:
#         grade = 'D'
#     elif percentage >= 40:
#         grade = 'E'
#     else:
#         grade = 'Fail'    

#     print('====================')
#     print(f"Student Id: {sId}")
#     print(f"Total marks: {total}")
#     print(f"percentage: {percentage}")
#     print(f"Grade: {grade}")
#     sId += 1
#     print('===================')


# data = [
#     {'name': 'ram', 'gender': 'male'},
#      {'name': 'sophia', 'gender': 'female'},
#       {'name': 'ram', 'gender': 'male'}
# ]
# male = 0
# female = 0
# for user in data:
#     if user['gender'] == 'male':
#         male += 1
#     else:
#         female +=1
# print(f"Number of male: {male}\nNumber of female: {female}")

# number_of_time = int(input("Enter number of times: "))
# x=1
# data = []

# while x<= number_of_time :
#     name = input("Enter your name: ")
#     gender = input("Enter your gender: ")
#     new_data = {"name": name, "gender": gender}
#     data.append(new_data)
#     x+=1
# total_male = 0
# total_female = 0
# for user in data:
#     if user['gender'] == 'male':
#         total_male +=1
#     else:
#         total_female +=1
# print(total_male)
# print(total_female)


# data = [
#     {
#         'name': 'ram',
#         'address':
#             {
#                 'city': 'kathmandu',
#             }
#     },
#     {
#         'name': 'sita',
#         'address': {
#             'city': 'bhaktapur',
#         }
#     },
#     {
#         'name': 'hari',
#         'address': {
#             'city': 'lalitpur',
#         }
#     },
# ]
# increment=0
# name = {}
# addres = {}
# city = {}
# for user in data:
#     name = data[increment]['name']
#     city = data[increment]['address']['city']
#     print(f"My name is {name} and city is {city}")
#     increment +=1

# data = [
#     {'name': 'ram', 'gender': 'male', 'status': True},
#     {'name': 'sophia', 'gender': 'female', 'status': False},
#     {'name': 'rita', 'gender': 'female', 'status': True},
#     {'name': 'laxmi', 'gender': 'female', 'status': True},
#     {'name': 'kabita', 'gender': 'female', 'status': True},
#     {'name': 'gopal', 'gender': 'male', 'status': False},
# ]
# total = 0
# active_user = 0
# inactive_user = 0
# name = {}
# gender = {}
# status = {}
# for user in data:
#    name = user['name']
#    gender = user['gender']
#    status = user['status']
#    print(f"name is {name} gender is {gender} and status is {status}")
#    total +=1
   
   
#    if status == True:
        # active_user +=1
#       print("active user")
#    else:
    #  inactive_user +=1
#       print("inactive user")
      
      

# print(f"total {total}")

# for user in data:

# total users
# total active users
# total inactive users
# total active male
# total inactive male   
# total active female
# total inactive female

# data = [
#     {'name': 'ram', 'gender': 'male', 'status': True},
#     {'name': 'sophia', 'gender': 'female', 'status': False},
#     {'name': 'rita', 'gender': 'female', 'status': True},
#     {'name': 'laxmi', 'gender': 'female', 'status': True},
#     {'name': 'kabita', 'gender': 'female', 'status': True},
#     {'name': 'gopal', 'gender': 'male', 'status': False},
# ]

# total_users = 0
# total_active_users = 0
# total_inactive_users = 0
# total_active_male = 0
# total_inactive_male = 0
# total_active_female = 0
# total_inactive_female = 0

# for users in data:
#     status = users['status']
#     gender = users['gender']
#     if status == True:
#         total_active_users +=1
#         if gender=='male':
#             total_active_male += 1
#         else:
#             total_active_female += 1
#     else:
#         total_inactive_users += 1
#         if gender=='male':
#             total_inactive_male += 1
#         else:
#             total_inactive_female += 1
#     total_users +=1 

# print(f"Total number of users: {total_users}")
# print(f"Total number of active users: {total_active_users}")
# print(f"Total number of inactive users: {total_inactive_users}")
# print(f"Total number of active male users: {total_active_male}")
# print(f"Total number of active female users: {total_active_female}")
# print(f"Total number of inactive male users: {total_inactive_male}")
# print(f"Total number of inactive female users: {total_inactive_female}")


# number = [1, 29, 3, 4, 5, 6, 78, 88, 9, 10]
# largest_number = number[0]
# smallest_number = number[0]
# for data in number:
#     if data> largest_number:
#         largest_number = data
#     if data<smallest_number:
#         smallest_number = data
# print(f"largest number {largest_number}")
# print(f"smallest number {smallest_number}")


# # function
# function is a block of code which is only run when it is called.

# types of function
# 1. built-in function : print() type () len() etc
# 2. user-defined function: function which is created by user.


# how to create a functiom?
#  def function_name():
#   block of Code 
#   block of Code 

# def greet():
#     print("Good Morning")

# greet()
  
# def greet(name):
#     print("Good morning", name)
# greet("susan")
# greet("sushan")


# def add():
#     x = 10
#     y = 8
#     print(" x + y : ", int(x) + int(y) )
# add()

# def substraction():
#     x = 10
#     y = 8
#     print(" x - y : ", int(x) - int(y))
# substraction ()


# def multiply():
#     x = 10
#     y = 8
#     print(" x * y : ", int(x) * int(y))
# multiply ()


# def division():
#     x = 10
#     y = 8
#     print(" x / y : ", int(x) / int(y))
# division ()

# def add(x, y):
#     print(x + y)
# add(10, 20)

# def user(name, age=0):
#     print("Name:", name)
#     print("age:", age)
# user('Rahul', 20)

# def user_info():
#     name = input("Enter your name : ")
#     email = input("enter your email: ")
#     address = input("enter your address: ")
#     phone = input("enter your phone: ")
#     city = input("enter your city: ")

#     print("----------------------------------")
#     print(f"your name is {name}")
#     print(f"your email is {email}")
#     print(f"your address is {address}")
#     print(f"your phone is {phone}")
#     print(f"your city is {city}")
# user_info()


# def add(x, y):
#     return x + y
# print(add(10,20))


# def users(*names):
#     print(names)

# users('ram', 'sita', 'hari')


# def total(*numbers):
#     total = 0
#     for number in numbers:
#         total = total + number
    
#     return total
# print(total(10,20,30,40,50))

# def users(*args, **kwargs):
#     print(args)
#     print(kwargs)
# users('ram', 'sita', 'hari', name = 'sachin')



# add = lambda a,b: a+b
# print(add(10,20))


# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(10))
