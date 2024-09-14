#ACCES  MODIFIER IN PYTHON :
#publish access:

# class employee :
#     def __init__(self):
#         self.name = "paras"
# a = employee()
# print(a.name)

#private access :
class employee :
    def __init__(self):
        self.__name = "paras2"
a = employee()
print(a._employee__name) #name mangling

#protecting access :
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())

#Static method in python :

class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n
    
  @staticmethod
  def add(a, b):
      return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7, 2)) 

#Class variable and instance variable:
class Employee:
    def __init__(self,name):
     self.name = name
    def showdetails(self):
        print(f"the name is employee {self.name}")
emp1= Employee("paras")
Employee.showdetails(emp1)        
#emp1.showdetails

class Employee:
  companyName = "Apple"
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name
    self.raise_amount = 0.02
    Employee.noOfEmployees +=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India" 
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()

#exercise:
# Write a Library class with no_of_books and books as two instance variables.
#  Write a program to create a library from this Library class and show how you can print all books,
#   add a book and get the number of books using different methods.
#    Show that your program doesnt persist the books after the program is stopped!

class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
      print(book)


l1 = Library()
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")
l1.showInfo()
    
  