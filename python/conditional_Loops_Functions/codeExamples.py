
# If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")


# One line if statement:

if a > b: print("a is greater than b")


# One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")



# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1



# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# Loop through the letters in the word "banana":

for x in "banana":
  print(x)



# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)



# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)





# example for function defination
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")


# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")





# The following example shows how to use a default parameter value.

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")




# using list as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)




























































