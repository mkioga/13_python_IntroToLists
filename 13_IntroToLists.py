
# ====================
# 13_IntroToLists.py
# ====================


# SEQUENCE TYPES
# We have already looked at str (string) sequence type
# Python has 6 other built in sequence types
# These are: lists, range, tuple,
# Here is a list of operations that can be ran on the sequences
# 4.6.1. Common Sequence Operations
# https://docs.python.org/3/library/stdtypes.html

# So far we have used the first 8 operations in this list
# example of an operation is s.count(x)
# to count total number of occurances of x in s

ipAddress = input("Please enter an IP address: ")
print(ipAddress.count(".")) # we want to count the number of periods

# =======
# LISTS:
# =======

# lists are sequence of things e.g. strings, numbers, classes, etc
# since a string is a sequence of letters, then a list can be a sequence of lists.

# Ways to create lists
# (1) Enclosing them in square brackets

# Example of a list of strings

print("="*20)
parrotList = ["not good", "very good", "not bad", "super bad"] # A list
for state in parrotList:
    print("This parrot is "+ state) # concantenate since state is string


# How to append to a list
# We are going to append "really good" to above list
# When you ran the code, it will show the appended string

print("="*20)
parrotList = ["not good", "very good", "not bad", "super bad"] # A list
parrotList.append("really good")

for state in parrotList:
    print("This parrot is "+ state) # concantenate since state is string



# (2) concatenating or appending existing lists


# List of numbers of integers

print("="*20)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd # Concatenantes lists even if they are numbers
print(numbers)


# (3) Using a function like sort to return a list

# results above are not in order.
# If we want to sort the result from smallest to largest, we use sort method

print("="*20)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd # Concatenantes lists even if they are numbers
numbers.sort()  # sort method sorts the concatenated numbers from smallest to largest
print(numbers)

# Note that sort method in python only works on existing object, in this case numbers
# but it does not create an object on its own.
# So this code below will not work

print("="*20)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd # Concatenantes lists even if they are numbers
print(numbers.sort()) # supposed to create object, but sort in python does not create objects


# sorted function
# If you want to create a new object instead of using the one you have
# you can use the "sorted" function to sort the new created object

print("="*20)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
print(sorted(numbers))

# you can assign the new sorted object to a variable and use it.
# in this case, we assign it to sortedNumbers

print("="*20)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
sortedNumbers = (sorted(numbers))
print(sortedNumbers)

# We can test to compare if numbers (unordered) and sortedNumbers are equal
# in python, they are not, because they are different sequences

print("="*20)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
sortedNumbers = (sorted(numbers))
print(sortedNumbers)

if numbers == sortedNumbers:
    print("Numbers are equal")
else:
    print("Numbers are Not equal")


# We can also check the sorted numbers to verify they are equal

print("="*20)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
sortedNumbers = (sorted(numbers))
print(sortedNumbers)

if sortedNumbers == sorted(numbers):
    print("Numbers are equal")
else:
    print("Numbers are Not equal")


# (4) Create list using list constructor
# list constructor is the built in function list()

# Here we will create two empty lists
# if you print them, they will have nothing, just []

print("="*20)
list_1 = []      # using square brackets
list_2 = list()  # using list constructor

print("List_1: {}".format(list_1))
print("List_2: {}".format(list_2))

if list_1 == list_2:
    print("The lists are equal") # lists will be equal because they are both null


# list() can be called without parameters as above
# But we can also call it with a single iterable parameter
# An iterable parameter is an object that is capable of returning its members one at a time
# All the sequence types built in python are iterable.
# We can pass a string to the list() like this
# The result here show python has created a list with the string we gave it one character
# at a time

print("="*20)
print(list("Good Morning"))


# This can be useful if you want to assign a list() to another variable and have them
# reference a different list
# NOTE that when we assign even_1 to even_2, they now both point to same list in memory
# That is why when we reverse sort even_2, even_1 is also sorted
# Because they both refer to same list in memory

print("="*20)
even_1 = [2, 4, 6, 8]
even_2 = even_1      # assign even_1 to even_2 (They now refer to same list in memory)
print(even_1 is even_2)  # This prints True because even_1 is same as even_2
even_2.sort(reverse=True)   # sort in reverse
print("even_1 is: {}".format(even_1))  # also sorted even if we sorted even_2 only
print("even_2 is: {}".format(even_2))



# We can create new list (even_2) and pass it parameter using list constructor list(even_1)
# The list constructor returns a new list and therefore we have two lists.
# Then even_1 will not be same as even_2 although their contents are same
# This is because they are now refereing to different lists in memory.
# This is why even_2 gets sorted and even_1 remains unsorted

print("="*20)
even_1 = [2, 4, 6, 8]
even_2 = list(even_1)  # New list even_2 assigned contents of list(even_1)
print(even_1 is even_2) # prints False because even_1 & even_2 points to different variables in memory
print(even_1 == even_2) # prints true because their contents are same even if pointing to different variables in memory
even_2.sort(reverse=True)   # sort even_2 in reverse
print("even_1 is: {}".format(even_1)) # even_1 remains unsorted
print("even_2 is: {}".format(even_2)) # even_2 is sorted



# we can also do this if we want a new version of even_2


print("="*20)
even_1 = [2, 4, 6, 8]
even_2 = sorted(even_1, reverse=True)

print(even_1 is even_2) # prints false because they are different variables in memory
print(even_1 == even_2) # prints false because they are now sorted in different order

even_2.sort(reverse=True)   # sort even_2 in reverse
print("even_1 is: {}".format(even_1)) # even_1 remains unsorted
print("even_2 is: {}".format(even_2)) # even_2 is sorted




# list within a list

print("="*20)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = [even, odd] # list named "numbers" is assigned list "even" and "odd"
print(numbers) # prints both lists one after the other


# we can run above code and use a for loop to get the individual numbers in the lists

print("="*20)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = [even, odd] # list named "numbers" is assigned list "even" and "odd"
print("numbers = {}".format(numbers))
for outer in numbers: # outer list: prints even and odd lists as blocks
    print("outer = {}".format(outer))
    for inner in outer: # inner list: prints individual numbers in even and odd
        print("inner = {}".format(inner))



# using for loop to search lists

print("="*20)
menu = []  # Empty list
menu.append(["egg", "spam", "bacon"])  # we append lists to main list menu
menu.append(["egg", "sausage", "bacon"])
menu.append(["spam", "beef", "chicken"])

print("menu = {}".format(menu)) # This prints the main list made of the small lists appended to it.
print()

for meal in menu:
    if not "spam" in meal:  # prints only the meal that has no spam in it.
        print("meal = {}".format(meal))




# Challenge
# add to program above to find meals without spam
# Then print the ingridients in the meal


print("="*20)
menu = []  # Empty list
menu.append(["egg", "spam", "bacon"])  # we append lists to main list menu
menu.append(["egg", "sausage", "bacon"])
menu.append(["spam", "beef", "chicken"])

for meal in menu:
    if not "spam" in meal:  # prints only the meal that has no spam in it.
        print("meal = {}".format(meal))
        for ingredient in meal:
            print("ingredient = {}".format(ingredient))




