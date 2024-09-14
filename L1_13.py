#class and object:
# class person:
#     name = "paras"
#     occupation = "data sciencetist"
#     networth = 10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a =person()
# # a.name = "hitensh"       #name changing 
# # a.occupation = "CA"
# print(a.name,a.occupation)
# a.info()        

# # Creating an Object:
# class Details:
#     name = "Rohan"
#     age = 20

# obj1 = Details()
# print(obj1.name)
# print(obj1.age)

# # self parameter
# class Details:
#     name = "Rohan"
#     age = 20

#     def desc(self):
#         print("My name is", self.name, "and I'm", self.age, "years old.")

# obj1 = Details()
# obj1.desc()


# class Person:
#   name = "paras"
#   occupation = "data sciencetist"
#   networth = 10
#   def info(self):
#     print(f"{self.name} is a {self.occupation}")


# a = Person()
# b = Person()
# c = Person()

# a.name = "hitensh"
# a.occupation = "CA"

# b.name = "babita"
# b.occupation = "HR"

# # print(a.name, a.occupation)
# a.info()
# b.info()
# c.info()

# #constructor:
# class Person:

#   def __init__(self, name, occ):
#     print("Hey I am a person")
#     self.name = name
#     self.occ = occ

#   def info(self):
#     print(f"{self.name} is a {self.occ}")


# a = Person("Harry", "Developer")
# b = Person("Divya", "HR") 
# a.info()
# b.info()
# # print(a.name)
# # a.name = "Divya"
# # a.occ = "HR"
# # a.info()


#decorator:
def greet (fx):
  def mfx():
    print("Good morning")
    fx()
    print("Thanks for visit")
  return mfx

@greet
def hello():
  print("Hello world")

def add(a,b):
  print(a+b)
hello()  #or greet(hello)()

# getter and setter:
class MyClass:
    def __init__(self, value):
        self._value = value
    def show(self):
      print(f" value is {self._value}")

    @property
    def value(self):
        return self._value

obj = MyClass(10)
obj.show()


#setter:
class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
  @property
  def ten_value(self):
      return 10* self._value
    
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()

#inheritance:
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("paras", 4100)
e2.showDetails()
e2.showLanguage()
    


