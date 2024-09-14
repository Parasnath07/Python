# x = 4 
# print(x)



# def hello ():
#     x = 5
#     print(f" The local x is {x}")
#     print("hello paras") 
# print(f"The global x is {x}")
# hello()
# x = 5 
# print(f"the global x is {x}")    



# x = 10 # global variable

# def my_function():
#   y = 5 # local variable
#   print(y)

# my_function()
# print(x)
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

# how to change of x value :


# x = 10 # global variable

# def my_function():
#   global x
#   x = 4 # this will change the value of the global variable x
#   y = 5 # local variable

# my_function()
# print(x) # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function


#File handling:

f = open('myfile.txt','r')
text = f.read()
print(text)
f.close()     # creat file then read content


# # Writing to a File

# f = open('myfile.txt', 'w')
# f = open('myfile.txt', 'w')
# f.write('Hello, world!')
# Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.

# f = open('myfile.txt', 'a')
# f.write('Hello, world!')
# Closing a File
# It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.

# To close a file, you can use the close() method.

# f = open('myfile.txt', 'r')
# # ... do something with the file
# f.close()
# The 'with' statement
# Alternatively, you can use the with statement to automatically close the file after you are done with it.

# with open('myfile.txt', 'r') as f:

#     # ... do something with the file

#Read , readsline, write:
# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")

#   print(line)

f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

#seek() and tell() functions
# seek():

with open('file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5)

# tell() function
with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  f.seek(current_position)

# truncate() function
with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
  print(f.read())
