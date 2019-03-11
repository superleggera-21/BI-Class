# Printing output (can use single/double quotes)
print('Hello, World!')

#Single Line Comment
# """Python also has extended documentation capability, called docstrings.
# Docstrings can be one line, or multiline.
# Python uses triple quotes at the beginning and end of the docstring"""

#Indentation
if 5 > 2:
    print("Five is greater than two!")

#Variables
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

#To combine both text and a variable, Python uses the + character:
x = "awesome"
print("Python is " + x)

#If you try to combine a string and a number, Python will give you an error:
# x = 5
# y = "John"
# print(x + y)

#To verify the type of any object in Python, use the type() function:
x = 1    # int
y = 2.8  # float
z = "Hello"   # complex
print(type(x))
print(type(y))
print(type(z))

#Casting: Specify a Variable Type
y = int(2.8) # y will be 2
print(y)

#Strings
a = "Hello, World!"
#Get the character at position 1 (remember that the first character has the position 0)
print(a[1])
#Substring. Get the characters from position 2 to position 5 (not included)
print(a[2:5])
#The strip() method removes any whitespace from the beginning or the end
print(a.strip())
#The len() method returns the length of a string
print(len(a))
#Upper/Lower case
print(a.lower())
print(a.upper())
#The replace() method replaces a string with another string
print(a.replace("H", "J"))
#The split() method splits the string into substrings if it finds instances of the separator
print(a.split(","))

#Asking the user for input
print("Enter your name:")
x = input()
print("Hello, " + x)


#Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
thislist = ["apple", "banana", "cherry"]
print(thislist)

print(thislist[1])

thislist[1] = "blackcurrant"
print(thislist)

for x in thislist:
  print(x)

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

print(len(thislist))

thislist.append("orange")
print(thislist)

thislist.insert(1, "orange")
print(thislist)

thislist.remove("orange")
print(thislist)

# Python has a set of built-in methods that you can use on lists.
#
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Look up and practice rest of the collections
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# thistuple[1] = "blackcurrant"
# print(thistuple)

# Set is a collection which is unordered and unindexed. No duplicate members.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#Conditional Statements
#IF..ELSE
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#shorthand
print("b is greater than a") if b > a else print("a and b are equal") if a == b else print("a is greater than b")

#WHILE Loop
i = 1
while i < 6:
  print(i)
  i += 1


#With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#With the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# FOR Loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
    print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# Dates
import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# A reference of all the legal format codes:

# Directive	Description	                            Example
# %a	    Weekday, short version	                Wed
# %A	    Weekday, full version	                Wednesday
# %w	    Weekday as a number 0-6, 0 is Sunday	3
# %d	    Day of month 01-31	                    31
# %b	    Month name, short version	            Dec
# %B	    Month name, full version	            December
# %m	    Month as a number 01-12	                12
# %y	    Year, short version, without century	18
# %Y	    Year, full version	                    2018
# %H	    Hour 00-23	                            17
# %I	    Hour 00-12	                            05
# %p	    AM/PM	                                PM
# %M	    Minute 00-59	                        41
# %S	    Second 00-59	                        08
# %f	    Microsecond 000000-999999	            548513
# %z	    UTC offset	                            +0100
# %Z	    Timezone	                            CST
# %j	    Day number of year 001-366	            365
# %U	    Week number of year, Sunday as the first day of week, 00-53	52
# %W	    Week number of year, Monday as the first day of week, 00-53	52
# %c	    Local version of date and time	Mon Dec 31 17:41:00 2018
# %x	    Local version of date	12/31/18
# %X	    Local version of time	17:41:00
# %%	    A % character	        %



# Functions

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def my_function():
  print("Hello from a function")

my_function()

#The following example has a function with one parameter (fname)
def my_function1(fname):
  print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

#If we call the function without parameter, it uses the default value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#To let a function return a value, use the return statement
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# Classes

class Dog():
#Represent a dog.
 def __init__(self, name):
 #Initialize dog object.
    self.name = name
 def sit(self):
 #Simulate sitting.
    print(self.name + " is sitting.")
my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
my_dog.sit()

# Inheritance
class SARDog(Dog):
#Represent a search dog.
 def __init__(self, name):
#Initialize the sardog.
    super().__init__(name)
 def search(self):
#Simulate searching.
    print(self.name + " is searching.")
my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()
