# for multi line strings
# You can use three double quotes or single quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])


# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)


# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)


# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

# Use negative indexes to start the slice from the end of the string:
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])


# example of strip method
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# eg of split method
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# string concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)



# Use the format() method to insert numbers into strings:
# eg1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# eg2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))





#Program to reverse a string
gfg = "geeksforgeeks"
print(gfg[::-1])


# We can also reverse a string by using built-in join and reversed function.


# Program to reverse a string
 
gfg = "geeksforgeeks"
 
# Reverse the string using reversed and join function
gfg = "".join(reversed(gfg))
 
print(gfg)





# Python Program to Update
# character of a String
 
String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)
 
# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
### there are following two ways
#1
list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)
 
#2
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)



































































































































