
# printing on the same line
# for printing on the same line use
# end parameters of the print function
# end takes the values which is printing
# at the end of the output.
print(1, end=" ")
print(2)
# op = 1 2


# example for user input
username = input("Enter username:")
print("Username is: " + username)

# example for multiple values for formatting
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# example 2
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# example 3
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))



# Python3 program to get input from user
  
# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
  
num3 = num1 * num2
print("Product is: ", num3)


# user input for int and float 
num = int(input("Enter a number: "))
print(num, " ", type(num))
 
           
floatNum = float(input("Enter a decimal number: "))
print(floatNum, " ", type(floatNum))



# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()




# taking multiple inputs at a time 
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x) 







# Python program showing how to use
# string modulo operator(%) to print
# fancier output

# print integer and float value
print("Geeks : %7d, Portal : %5.2f" % (105, 05.333))

# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120))

# print octal value
print("%7.3o" % (25))

# print exponential value
print("%10.3E" % (356.08977))



# o/p 
# Geeks :     105, Portal :  5.33
# Total students : 240, Boys : 120
#     031
#  3.561E+02

# explanation 
# The first placeholder “%2d” is used for the first component of our tuple, i.e. the integer 1.
# The number will be printed with 2 characters. As 1 consists only of one digit, the output is padded with 
# 1 leading blanks.
# The second one “%5.2f” is a format description for a float number. 
# Like other placeholders, it is introduced with the % character. This is followed by 
# the total number of digits the string should contain. This number includes the decimal 
# point and all the digits, i.e. before and after the decimal point.
# Our float number 05.333 has to be formatted with 5 characters.
# The decimal part of the number or the precision is set to 2, i.e. the number following the “.” in our 
# placeholder. Finally, the last character “f” of our placeholder stands for “float”.





# Python program showing
# use of format() method
 
# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
 
# using format() method and referring
# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))
 
print('{1} and {0}'.format('Geeks', 'Portal'))
 
 
# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.
 
print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
 
# using format() method and referring
# a position of the object
print(f"{'Geeks'} and {'Portal'}")

# op
# I love Geeks for "Geeks!"
# Geeks and Portal
# Portal and Geeks
# I love Geeks for "Geeks!"
# Geeks and Portal





# Python program showing
# a use of format() method

# combining positional and keyword arguments
print('Number one portal is {0}, {1}, and {other}.'
	.format('Geeks', 'For', other ='Geeks'))

# using format() method with number
print("Geeks :{0:2d}, Portal :{1:8.2f}".
	format(12, 00.546))

# Changing positional argument
print("Second argument:{1:3d}, first one: {0:7.2f}".
	format(47.42, 11))

print("Geeks: {a:5d}, Portal: {p:8.2f}".
	format(a = 453, p = 59.058))


# op
# Number one portal is Geeks, For, and Geeks.
# Geeks :12, Portal :    0.55
# Second argument: 11, first one:   47.42
# Geeks:   453, Portal:    59.06



