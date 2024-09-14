#if_else statement:
#a = int(input("enter your age "))
#print("your age is ",a)
##
#else:
    ##print("no")

#elif statement:
# appleprice = 70
# budget = 200
# if(budget - appleprice > 50):
#     print("paras,you can buy to apple")
# else:
#     print("you can not buy apple")

# #elif:
# num = int(input("enter your choice number "))
# if(num < 0):
#     print("number is negative")
# elif(num == 0):
#     print("number is zero ")
# elif(num == 1000):
#     print("i am lucky")
# else:
#     print("number is positive")

# nested: (do not understand revised again :)
# num = 18
# if (num < 0):
#     print ("number is negative.")
# elif(num > 0):
#     if(num <= 10):
#         print("number is between 1-10")
#         elif (num >10 and num <=20):
#             print("number is between 11-20")
#             else:
#                 print("number is greater than 20")
# else:
#     print("number is zero") 
#exercise 2:
import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# good morning, good evening, good night 
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("enter your time: "))
print(hour)
if(hour>=0 and hour<12):
    print("good morning!")
    

#match case statement :
# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")
#     case _:
#         print(x)
# Loop in python
# name = 'parasnath'
# for i in name:
#  print(i)
#  if(i=="s"):
#   print("this is something special")

# #list in loop 
# fruit = ["apple","banana","mango"]
# for frutty in fruit:
#     print(frutty)
#     for i in frutty:
#         print(i)

#range()

# for k in range(5):
#     # print(k)
#     print(k+1)

# for k in range(1,50):
#     print(k)

# explore about third parameter of range(range(4,7,8))
# for k in range(1,12,3):
#     print(k)

# while in loop :
# i = 0
# while(i<3):
#     print(i)
#     i = i + 1

# while(i<=3):
#     print(i)
#     i = i + 1

# i = int(input("enter your number: "))
# while(i<=38):
#     i= int(input("enter your nomber: "))
#     print(i)
# print("done your chance")


j = 8
while(j>0):
    print(j)
    j = j - 1

j = 8
while(j>0):
    print(j)
    j = j - 1
else:
    print("your work is completed")  

# break statement: move to loop
# for i in range (12):
#     print("5 X",i+1,"=",5*(i + 1))
#     if(i==10):
#         break
# print("your are exit ")

# for i in range (12):
#     if(i==10):
#         break
#     print("5 X",i+1,"=",5*(i + 1))
# print("your are exit ")

#continue : move to iteration

for i in range (12):
    if(i==10):
        print("skip to number")
        continue
    print("5 X",i,"=",5*(i))




    