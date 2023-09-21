
# example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])



# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)





# The values in dictionary items can be of any data type:
# Example
# String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


# Get the value of the "model" key:
x = thisdict.get("model")



# Get a list of the keys:

x = thisdict.keys()



# get the list of the values
x = thisdict.values()


# eg for items method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)


# Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018



# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# popitem() method eg
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)



# The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)



# Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])



# Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)



# Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)




# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}




# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(a, b, c):
    print(a, b, c)
 
# A call with unpacking of dictionary
d = {'a':2, 'b':4, 'c':10}
fun(**d)





# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
 
    # kwargs is a dict
    print(type(kwargs))
 
    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))
 
# Driver code
fun(name="geeks", ID="101", language="Python")


























































