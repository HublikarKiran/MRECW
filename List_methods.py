# list is first in first out data structure
# creating List

lists = [1, 2, 3]
print(lists)


for i in lists:
    print(i)

# creating list using iterables

list_range = range(5)  # range(0,5)
print(list_range)

list_range = list(range(5))  # [0,1,2,3,4]
print(list_range)


# accessing elements from the list

element = lists[0], lists[1], lists[2]  # but this creates tuples
single_element = lists[0]      # single element is int type
print(element)
print(type(element))


# adding elements to a list using append method and extend method

lists.append("hello")
print(lists)

lists.extend([7, 8])
print(lists)

# removing last element from a list using pop() method

lists.pop()
print(lists)

# removing specific element from a list using remove() method
lists.remove(2)
print(lists)

# reversing a list using reverse() method
lists.reverse()
print(lists)

# sorting a list using sort() method
# lists.sort()  # this is in lists =[7, 'hello', 3, 1]
# print(lists)  # lists.sort()  TypeError: '<' not supported between instances of 'str' and 'int'

lists.remove('hello')
print(lists)

# now we can use sort() method
lists.sort()
print(lists)  # Output : [1, 3, 7]

# finding length of a list using len() function

print(len(lists))


lists.append(10)
print(lists)


lists.append(["hi", "bye"])  # it will add as one element
print(lists)

# to add multiple elements at once we need to use extend()
lists.extend(["hi", "bye"])  # each element will be added separately
print(lists)

# to find index of an element in a list
print(lists.index('hi'))  # output : 5
print(lists.index(7))  # output : 2

# this count how many times that number appears in a list

print(lists.count(1))  # output : 1
print(lists.count(10))  # output : 1

# copy a list into another list using copy() method
new_lists = lists.copy()
print(new_lists)
reverse = lists.reverse()

# list.copy() → creates a new list and returns it. It does not modify the existing list.
# list.reverse() → reverses the list in place and returns None.
print(reverse)  # returns None because there is no return value for reverse()
print(lists)  # returns reversed list because it changes original list also


# clear all elements from a list using clear() method
lists.clear()
print(lists)

# create a list with same values repeated n times using * operator
a = [1]*5
print(a)  # output : [1, 1, 1, 1, 1]

b = ['hi']*5
print(b)  # output : ['hi', 'hi', 'hi', 'hi', 'hi']

c = [[1]]*5
print(c)  # output : [[1], [1], [1], [1], [1]]
# this is wrong way to create a list with same values repeated n times because it will create a reference to the same object
# creating like this  [[1]]*5 means [[1],[1],[1],[1],[1]] which is wrong
# because element inside list like this [1]] is mutable so if you change any element then other elements will also get changed
d = [[1]*5]*5
# output : [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
print(d)
e = [[i]*5 for i in range(5)]
# output : [[0, 0, 0, 0, 0], [1 , 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
print(e)


is_present = 3 in [1, 2, 3, 4, 5]   # checks whether 3 is present in the list or not
print("Check if 3 in list:", is_present)

max_val = max([1, 2, 3, 4, 5])   # prints maximum value from the list
min_val = min([1, 2, 3, 4, 5])
print("Max value:", max_val, "Min value:", min_val)

total = sum([1, 2, 3, 4, 5])
print("Sum of list:", total)

# slicing a list
print(lists[:])     # output : [] because lists is empty
print(lists[::-1])   # output : []

lists = list(range(1, 6))
print(lists)         # output : [1, 2, 3, 4, 5]
# output : [1, 3, 5]           because it starts from 0 and goes till end by skipping every second element
print(lists[::2])
# output : [5, 4, 3, 2, 1]   because it starts from -1 and goes till start
print(lists[-1::-1])
# output : []                 it is empty  because it starts from start and goes to last directly not from right side but from left side
print(lists[:-1:-1])
print(lists[::-1])   # output : [5, 4, 3, 2, 1]     printing reversed list
# output : [5, 3, 1]              printing reversed list by skipping every second element
print(lists[::-2])


# concatenating two lists using + operator
lists = list(range(1, 6))
print(lists)          # output : [1, 2, 3, 4, 5]
print(lists+lists)    # output : [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(lists*2)        # output : [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# checking whether an element exists in a list or not using in keyword
print(1 in lists)       # output : True
print(10 in lists)      # output : False


import copy
shallow_copy = copy.copy(my_list)
deep_copy = copy.deepcopy(my_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)

print("--------------------")
# iterating over a list using for loop
for i in lists:
    print(i)            # output : 1, 2, 3, 4, 5

print("--------------------")
# iterating over a list using while loop
i = 0
while i < len(lists):
    print(lists[i])     # output : 1, 2, 3, 4, 5
    i += 1
print("--------------------")


# converting string to list using split() method    split() method splits a string into a list
string = "Hello World"
# output : ['Hello', 'World']  #here space is default delimiter
print(string.split())
# output : ['Hello', 'World'] #here space is delimiter means it will split wherever space occurs
print(string.split(" "))


s = "Hello   World"
print(s.split())      # ['Hello', 'World']
# ['Hello', '', '', 'World']  #Here you explicitly tell Python to split only on a single space " ".
print(s.split(" "))

# converting list to string using join() method
print("".join(['Hello', 'World']))  # output : HelloWorld
# output : Hello-World because "-" is used as delimiter here
print("-".join(['Hello', 'World']))
# output : Hello World because " " is used as delimiter here
print(" ".join(['Hello', 'World']))
# output : Hello\nWorld because "\n" prints in next line because \n is newline character
print("\n".join(['Hello', 'World']))
# output : Hello, World because ", " is used as delimiter here
print(", ".join(['Hello', 'World']))
# output : Hello World because " " is used as delimiter he
print("".join(['Hello', ' ', 'World']))
# output : Hello	World because "\t" takes tab space
print("".join(['Hello', '\t', 'World']))
# output : Hello\nWorld because "\n" prints next line
print("".join(['Hello', '\n', 'World']))
# output : Hello\rWorld because "\r"  prints carriage return
print("".join(['Hello', '\r', 'World']))
# output : Hello\fWorld because "\f"  prints form feed means page break
print("".join(['Hello', '\f', 'World']))


# nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)             # output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# accessing elements from nested list
print(nested_list[0][0])       # output : 1
print(nested_list[1][2])       # output : 6
print(nested_list[2][1])       # output : 8

# accessing elements from nested list using for loop
for i in nested_list:
    for j in i:
        print(j)               # output : 1, 2, 3, 4, 5, 6, 7, 8, 9

for i in nested_list:
    for j in i:
        print(j, end=" ")    # output : 1 2 3 4 5 6 7 8 9
    print()

# accessing elements from nested list using while loop
i = 0
while i < len(nested_list):
    j = 0
    while j < len(nested_list[i]):
        print(nested_list[i][j])   # output : 1, 2, 3, 4, 5, 6, 7, 8, 9
        j += 1
    i += 1


