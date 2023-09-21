


# The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()



# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)



# Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)



# Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)


# The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
# Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])



# Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)


# Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))