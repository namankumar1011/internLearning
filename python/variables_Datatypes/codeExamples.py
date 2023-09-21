
#This is how python variables are assigned 
#Example:
x = 5
y = "Hello, World!"
print(x)
print(y)

# we can change the type of variable
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)



# example to get the type of a variable
x = 5
y = "John"
print(type(x))
print(type(y))


# legal variablre names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"


# assign multiple values to variables 
x, y, z = "Orange", "Banana", "Cherry"

# one value to multiple variables
x = y = z = "Orange"



# Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



# In the print() function, you output multiple variables, separated by a comma:
# Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# same can be done with + operator
x = "Python "
y = "is "
z = "awesome"
print(x+ y+ z)


# this will give an error that operands are not of the same kind
x = 5
y = "John"
print(x + y)

# however we can overcome this by using ,
x = 5
y = "John"
print(x ,y)


# example for local and global variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# example of global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Print the data type of the variable x:
x = 5
print(type(x))




# example of int type
x = 1
y = 35656222554887711
z = -3255522

# example of float type
x = 1.10
y = 1.0
z = -35.59


# example for complex
x = 3+5j
y = 5j
z = -5j



# example to generate random nos.
import random

print(random.randrange(1, 10))