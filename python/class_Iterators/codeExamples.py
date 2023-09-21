
# example of class and object
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)



# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)


# example of object methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



# Delete the age property from the p1 object:

del p1.age


# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass


# using the super() function to inherit the parent class methods
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)



# Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))








































































































