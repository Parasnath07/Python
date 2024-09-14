# dictionary :
dic = {"paras":"is boy ", "india": "loves"}
print(dic["paras"])

info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  
#Accessing single values:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

#Accessing multiple values:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

#Accessing keys:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

#Accessing key-value pairs:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

#method of dictionary:
ep1 = {123:45,467:67,784:78}
ep2= {345:89,678:82,234:10}
# ep1.update(ep2)
# print(ep1)
# ep1.clear()
# print(ep1)
# ep1.pop(123)
# print(ep1)
ep1.popitem()
print(ep1)
del ep1[123]
print(ep1)


## for loop with else in  python:

for i in range(5):
  print(i)
else:
  print("sorry no i")  


for i in range(6):
  print(i)
  if i == 4:
    break
else:         # complete run code but not print else content
  print("sorry no i")  

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")  

