#short hand if else statement:
# a = 1300
# b = 400
# print("A")if a>b else print ("=")if a==b else print("B")

# c = 9 if a>b else 0 
# print (c)
#enumarate function in python :
# marks = [12,14,50,79,98,45,80]
# index = 0 
# for mark in marks:
#     print(mark)
#     if (index ==3):
#         print("paras")
#     index +=1    

  
# for index,mark in enumerate(marks):
#     print(mark)
#     if (index ==3):
#         print("paras")
#     index +=1    

# #start index:
# for index,mark in enumerate(marks,start = 1):
#     print(mark)
#     if (index ==3):
#         print("paras")
#     index +=1    


#how import work in python:
# import math 
# result = math.sqrt(9)
# print(result)

# #from keyword:
# from math import  sqrt,pi
# result = math.sqrt(9)*pi   
# print(result)

# from math import *     #NOT RECOMBADED
# result = math.sqrt(9)*pi     
# print(result)

# tha "as" keyword:

# import math as m
# result = m.sqrt(10)*m.pi
# print(result)

# # the "dir" fuction:
# import math
# print(dir(math))

#if__name__=="__main__":
# def welcome():
#     print("your welcome from paras")
# if __name__=="__main__":
#      welcome()

#os module : in one folder built to large folder:

# import os
# for i in range(0,100): # multiple file creat in one folder
#     os.mkdir(f"data{i+1}") 

# #file rename:

# import os
# for i in range(0,100): 
#     os.rename(f"data/Day{i+1},",f"data/Day{i+1},") 


# #found folder:
# import os 
# folders = os.listdir("data")
# print (folders)
# for folder in folders:
#     print(os.listdir(f"data/{folder}"))
