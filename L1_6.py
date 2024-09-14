#exercise:
# Create a program capable of displaying questions to the user like KBC. 
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.
# question = ("who is present prime minister in india.")
# option= ("a. modi, b. nodi,c.godi,d.lodi")
# print(question)
# print(option)
# answer = input("enter your correct option")
# if answer==("a"):
#     print("cong.you won to 1crore")

# else:
#     print("best of luck")    

# string formating:

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "paras"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))

#docs string:
def square(n):
    '''Take in a number n, return square of n'''
    print(n**2)
square(5)  
print(square.__doc__)  

# recursion in python:
def factorial(n):
    if (n == 1 or n == 0):
       return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))     

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....
#exercise:

# def fib (n):
#     if(n==0):
#      return 0
#     elif(n==1):
#      return 1
#     else:
#         return fib(n-1)+fib(n-2)   
# y = int(input("enter your choice number:")) 
# print(fib(y))

