# import time 

# def usingWhile():
#   i = 0
#   while i<50000:
#     i = i +1
#     print(i) 

# def usingFor():
#   for i in range(50000):
#     print(i)

# init = time.time()
# usingFor()
# t1 = time.time() - init
# init = time.time()
# usingWhile()
# print(time.time() - init)
# print(t1)

# print(4)
# time.sleep(3)
# print("print after three sec.")
 #time.str:
# t = time.localtime()
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

# print(formatted_time) 

# #The Walrus Operator in Python:
# numbers = [1, 2, 3, 4, 5]

# while (n := len(numbers)) > 0:
#     print(numbers.pop())

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = False
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)
# foods = list()
# while (food := input("What food do you like?: ")) != "quit":
#     foods.append(food)   

#shutil:
# import shutil
# shutil.copy("L1_17.py","L1_172.py")
# The following are some of the most commonly used functions in the shutil module:

# shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.

# shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

# shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

# shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

# shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell.

# Examples
# Here are some examples of how you can use the shutil module in your Python code:

# import shutil
# # Copying a file
# shutil.copy("src.txt", "dst.txt")
# # Copying a directory
# shutil.copytree("src_dir", "dst_dir")
# # Moving a file
# shutil.move("src.txt", "dst.txt")
# # Deleting a directory
# shutil.rmtree("dir")

#Requests module in python:
import requests
response = requests.get("https://www.google.com")
print(response.text)

#Post Request/bs4 module::
import requests 
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)