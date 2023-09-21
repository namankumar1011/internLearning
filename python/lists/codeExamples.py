# eg
mylist = ["apple", "banana", "cherry"]
print(mylist)


# List items can be of any data type:
# String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]
print(list1)


# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])



# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])



# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])



# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)



# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)



# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)



# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# eg for del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)



# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# using range and len
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# using while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)




# with list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]


# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)




# Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)



# custom sort function
# Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# reverse a list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)




# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)



# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)



# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)




# Python program to take space
# separated input as a string
# split and store it to a list
# and print the string list
 
# input the list as string
string = input("Enter elements (Space-Separated): ")
 
# split the strings and store it to a list
lst = string.split() 
print('The list is:', lst)   # printing the list







# Python program to demonstrate
# Addition of elements in a List
  
# Creating a List
List = [1,2,3,4]
print("Initial List: ")
print(List)
 
# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)






# Reversing a list
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)





# A Python program to demonstrate both packing and
# unpacking.
 
# A sample python function that takes three arguments
# and prints them
def fun1(a, b, c):
    print(a, b, c)
 
# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):
 
    # Convert args tuple to a list so we can modify it
    args = list(args)
 
    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'
 
    # UNPACKING args and calling fun1()
    fun1(*args)
 
# Driver code
fun2('Hello', 'beautiful', 'world!')







































































