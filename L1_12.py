# lembda function in python :

# def double(x):
#   return x*2

# def appl(fx, value):
#   return 6 + fx(value)

# double = lambda x: x * 2
# cube = lambda x: x * x * x
# avg = lambda x, y, z: (x + y + z) / 3

# print(double(5))
# print(cube(5))
# print(avg(3, 5, 10))
# print(appl(lambda x: x * x , 2))

#map ,filter:

#Map :
# def cube (x):
#     return x *x*x 
# print(cube(2))

l =[1,2,3,4,5,6,7,8]
# newl = list(map(cube.,l))
newl = list(map(lambda x: x*x*x , l))
print(newl)

#FILTER :
# def filter_function(a):
#     return a>5

# newnewl = list(filter(filter_function,l))
# print(newnewl)

#reduce :
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function

# sum = reduce(lambda x, y: x + y, numbers)
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print(sum)

#'is' vs '==' in Python:
# print(a is b) # exact location of object in memory
# print(a is None) # exact location of object in memory
# print(a == b) # value

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True

#exercise:

# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players
#  use hand gestures to represent a snake, water, or a gun. The gun beats the snake, 
#  the water beats the gun, and the snake beats the water. Write a python program to 
#  create a Snake Water Gun game in Python using if-else statements. 
#  Do not create any fancy GUI. Use proper functions to check for win.
n = random.randint(1,3):
inp = int(input("Enter your number"))
if inp == n:
    print("Draw")
elif inp == 3 and n == 1:
    print("comp wins")
elif inp == 1 and n == 3:
    print("Player wins")
elif inp > n:
    print("player wins")
elif inp < n:
    print("comp wins")
