# function in python :
# a = 9
# b = 8
# gmean1 = (a*b)/(a+b)
# print(gmean1)
# c = 8
# d = 7
# gmean2 =(c*d)/(c+d)
# print(gmean2)

# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print (mean)

# a = 7 
# b = 8
# if(a>b):
#     print("first number is greater")
# else:
#     print("second number is greater or equal")    
# calculateGmean(a,b)
# c = 9 
# d = 10
# calculateGmean(c,d)

# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print (mean)

# def isGreater (a,b):
#   if(a>b):
#     print("first number is greater")
#   else:
#     print("second number is greater or equal")    
# a = 7 
# b = 8
# isGreater(a,b)
# calculateGmean(a,b)
# c = 9 
# d = 6
# isGreater (c,d)
# calculateGmean(c,d)

#argument function:
# def average(a = 9 , b= 1 ):
#     print("the average is ",(a+b)/2)
# average(9,1)

# def average( a , b= 1 ):
#     print("the average is ",(a+b)/2)
# average(b=7)  
# #required argument:

# def name(pname,mname="paras",lname="kannaujiya"):
#     print("hello",pname,mname ,lname)
# name("njhhj","hshjike","jewuj9iuj") 

#arbitary argu.:
def name(*name):
    print("hello,",name[0],name[1],name[2])
name("gagan","magan","rohan")    
 
#keyword arbitary argument:
def name(**name):
    print("hello",name["bname"],name["sname"],name["hname"])
name(bname="hjghhg",sname="hijhkijhk",hname="uhwduh")


