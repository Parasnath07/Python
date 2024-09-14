#string in sciling & operation on string

name = "paras,engineer"
print(len(name))
print(name[0:4])
print(name[2:-4])
#quick quiz
nm = "harry"
print(nm[-4:-2])

#string method :
#Upper() :
a = "Paras"
print(a.upper())
#lower()
print(a.lower())

#rstrip()
b = "paras nath!!!!!!!!!!!!"
print(b.rstrip("!"))

#replace():
#c = "parasnath"
#print(c.replace("paras","viswa"))

#split()
d = "paras nath kannaujiya"
print(d.split(" "))
#CAPILATIZE():
e = "india is great"
print(e.capitalize())

#center():
f = "welcome to python !!1"
print(len(f))
print(f.center(50))
print(len(f.center(50)))

# count():
w = "paras paras nath "
print(w.count("paras"))

#endswith():
q = "lorika jaunpur !!!!!!"
print(q.endswith("!!!!!!"))
print(q.endswith("ik",3,5))

#find():
t = "darngiling chai"
print(t.find("g"))

#isalnum():
r = "ThereAreNotComplicated"
print(r.isalnum())

#isalpha():
y = "Welcome"
print(y.isalpha()) #: true

o = "welcome000"
print(o.isalpha())  #: false

#isprintable()
p = "i am good boy"
print(p.isprintable())
j = "i am very proud of you \n"
print(j.isprintable())
#isspace()
h = "      "
print(h.isspace())

#istitle():
k = "Honey Is So Sweet "
print(k.istitle())

i = "honey is so sweet"
print(i.istitle())

#if_else statement:
a = int(input("enter your age "))
print("your age is ",a)
if(a>18):
    print("you can drive")
    print("yes drive")
    print("yey!")
else:
    print("you can drive ")
    print("no")