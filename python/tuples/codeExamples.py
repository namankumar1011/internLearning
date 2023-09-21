
# example
mytuple = ("apple", "banana", "cherry")



# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")


# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)



# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)



# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)




# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)



# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)



# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)




# Below is an example that shows both packing and unpacking. 
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




























































