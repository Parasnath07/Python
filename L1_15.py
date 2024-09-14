# #Class method in python :
# class Employee:
#   company = "Apple"
#   def show(self):
#     print(f"The name is {self.name} and company is {self.company}")

#   @classmethod
#   def changeCompany(cls, newCompany):
#     cls.company = newCompany


# e1 = Employee()
# e1.name = "Harry"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)

# #class method as alternative constructor :
# class Employee:
#   def __init__(self, name, salary):
#     self.name = name 
#     self.salary = salary
    
#   @classmethod
#   def fromStr(cls, string):
#     return cls(string.split("-")[0], int(string.split("-")[1]))
    
# e1 = Employee("Harry", 12000)
# print(e1.name)
# print(e1.salary)

# string = "John-12000"
# e2 = Employee.fromStr(string)
# print(e2.name)
# print(e2.salary)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, string):
#         name, age = string.split(',')
#         return cls(name, int(age))

# person = Person.from_string("John Doe, 30")
# print(person.name, person.age)
# #__dir__ and__dict__:

# class Person:
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age
#       self.version = 1

    
# p = Person("John", 30)
# print(p.__dict__)

# print(help(Person)

# #__dir__:
# x = [1, 2, 3]
# dir(x)

#Super keyword in Python:
# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.1")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("parasnath")
#         super().parent_method()
#     def child_method(self):
#         print("This is the child method.2")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

# class Programmer(Employee):
#   def __init__(self, name, id, lang):
#     super().__init__( name, id)
#     self.lang = lang

# rohan = Employee("Rohan Das", "420")
# harry = Programmer("Harry", "2345", "Python")
# print(harry.name)
# print(harry.id)
# print(harry.lang)

#magic method:
# class Employee:
#     name = "parash"
#     def __len__(self):
#         i = 0
#         for c in self.name :
#             i = i+1
#         return i

# e = Employee()
# print(e.name)
# print(len(e))

#__str__ method:
class Employee:
    def __init__(self,name):
        self.name=name
    name = "parash"
    def __len__(self):
        i = 0
        for c in self.name :
            i = i+1
        return i
def __str__(self):
    return f"the name of the employee is {self.name}"

