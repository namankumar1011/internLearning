

# To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
# The code above is the same as:

f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
# Make sure the file exists, or else you will get an error.


# eg to open and read a file 
f = open("demofile.txt", "r")
print(f.read())

# Read one line of the file:

f = open("demofile.txt", "r")
print(f.readline())


# Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x)


# close the file when you are finish with it:

f = open("demofile.txt", "r")
print(f.readline())
f.close()


# Open the file "demofile2.txt" and append content to the file:

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())




# Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())



# Create a file called "myfile.txt":

f = open("myfile.txt", "x")


# Create a new file if it does not exist:

f = open("myfile.txt", "w")



# Remove the file "demofile.txt":

import os
os.remove("demofile.txt")



# Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")



# Remove the folder "myfolder": You can only remove empty folders.

import os
os.rmdir("myfolder")



