#overriding in python:
# class Shape:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
    
#   def area(self):
#       return self.x * self.y

# class Circle(Shape):
#     def __init__(self, radius):
#       self.radius = radius
#       super().__init__(radius, radius)

#     def area(self):
#         return 3.14 *  super().area()
      
# # rec = Shape(3, 5)
# # print(rec.area())

# c = Circle(5)
# print(c.area())

# #operator overloading in python:
# class vector:
#     def __init__(self,i,j,k):
#         self.i = i 
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
#     def __add__(self,x):
#         return vector(self.i+x.i,self.j+x.j,self.k+x.k )
# v1 = vector(4,6,7)
# print(v1)            

# v2 = vector(2,4,6)
# print(v2)
# print(v1+v2)


#single inheritance:
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class cat(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="cat")
        self.breed = breed
def make_sound(slef):
    print("myau")
c = cat("cat", "pitter")
c.make_sound()

a = Animal("cat", "cat")
a.make_sound()

#multiple inheritance:
class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())

#multilevel inheritance:
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = Dog("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())

# Example of Hybrid Inheritance 
class BaseClass:
  pass

class Derived1(BaseClass):
  pass  

class Derived2(BaseClass):
  pass  

class Derived3(Derived1, Derived2):
  pass

# Hierarchical Inheritance
class BaseClass:
  pass

class D1(BaseClass):
  pass

class D2(BaseClass):
  pass

class D3(D1):
  pass

#marged pdf file :
from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
