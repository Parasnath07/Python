#LIST:
# list = [5,6,7]
# print(list)
# print(list[0])
# print(list[1])
# print(list[2])

#negative index:
list = [5,6,7]
# print(list)
# print(list[0])
# print(list[-1])  #or(list[len(list)-1])
# print(list[-2])
# print(list[len(list)-1])

#checking:
if 7 in list:
    print("yes")
else:print("no")

if 9 in list:
    print("yes")
else: print("no")

#List comprehension:
# lst = [i for i in range(4)]
# print(lst)

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range (10)if i%2==0]
print(lst)

#method of list:
k = [1,2,3,4,3,3,3,5,6]
# k.append(7)
# k.sort() (increasing order)
# k.sort(reverse = True) #(decending order)
# k.reverse()   #(reverse)
# print(k.index(1))
# print(k.count(3))
# print(k.insert(1,897))
# n = [123,456,789]
# k.extend(n)
# print(k)

# #TUPLE
# tup = (2,56,7,7,"green")
# print(type(tup),tup)
# print(tup[1])
# print(tup[2])
# print(tup[3])

#manipulating tuple:

# countries = ("Spain","India","Russia","England","Germany")

# temp=list(countries)
# temp.append("China")  #for add
# temp.pop(3)    #for remove
# temp[2] = "Shree"   # change
# countries = teple(temp)
# print(countries)

# same rule on tupple

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)