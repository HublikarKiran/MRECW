# Python Tuples 
print("\n--- Creating Tuples ---")
my_tuple = (1, 2, 3, 4, 5)
print("Create a tuple:", my_tuple)

my_tuple2 = tuple([1, 2, 3, 4, 5])
print("Create tuple from list:", my_tuple2)

single_tuple = (42,)
print("Create tuple with single element:", single_tuple)

empty_tuple = ()
print("Empty tuple:", empty_tuple)

print("\n--- Accessing Elements ---")
element = my_tuple[0]
print("Access element at index 0:", element)

last = my_tuple[-1]
print("Negative indexing (last element):", last)

sub_tuple = my_tuple[1:4]
print("Slicing [1:4]:", sub_tuple)

print("\n--- Tuple Operations ---")
new_tuple = my_tuple + (6, 7, 8)
print("Concatenate tuples:", new_tuple)

repeated = my_tuple * 3
print("Repeat tuple *3:", repeated)

a, b, c = (1, 2, 3)
print("Unpack tuple (a, b, c):", a, b, c)

a, *rest = (1, 2, 3, 4, 5)
print("Unpack with * (a, *rest):", a, rest)

a, b = 1, 2
a, b = b, a
print("Swap values:", a, b)

nested = ((1, 2), (3, 4))
print("Nested tuples:", nested)

print("\n--- Tuple Methods ---")
count = my_tuple.count(2)
print("Count occurrences of 2:", count)

index = my_tuple.index(3)
print("Index of element 3:", index)

print("\n--- Membership Tests ---")
exists = 3 in my_tuple
print("Check if 3 exists:", exists)

not_exists = 10 not in my_tuple
print("Check if 10 not exists:", not_exists)

print("\n--- Tuple Properties ---")
length = len(my_tuple)
print("Length of tuple:", length)

max_val = max(my_tuple)
min_val = min(my_tuple)
print("Max:", max_val, "Min:", min_val)

total = sum(my_tuple)
print("Sum of tuple:", total)

print("\n--- Sorting ---")
sorted_tuple = sorted(my_tuple)
print("Sorted tuple (returns list):", sorted_tuple)

sorted_desc = sorted(my_tuple, reverse=True)
print("Sorted descending:", sorted_desc)

print("\n--- Conversions ---")
tuple_from_list = tuple([1, 2, 3])
print("Convert list to tuple:", tuple_from_list)

tuple_from_string = tuple("Hello")
print("Convert string to tuple:", tuple_from_string)

print("\n--- Advanced Operations ---")
zipped = tuple(zip((1, 2, 3), ('a', 'b', 'c')))
print("Zip tuples:", zipped)

for index, value in enumerate(my_tuple):
    print(f"Enumerate: index={index}, value={value}")

filtered = tuple(filter(lambda x: x % 2 == 0, my_tuple))
print("Filter even numbers:", filtered)

mapped = tuple(map(lambda x: x * 2, my_tuple))
print("Map function (double each):", mapped)

print("\n--- Boolean Checks ---")
any_true = any(my_tuple)
print("Any true in tuple:", any_true)

all_true = all(my_tuple)
print("All true in tuple:", all_true)






# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Create tuple from list
my_tuple = tuple([1, 2, 3, 4, 5])
print(my_tuple)

# Create tuple with single element
single_tuple = (42,)
print(single_tuple)

# Create empty tuple
empty_tuple = ()
print(empty_tuple)

# Access element
element = my_tuple[0]
print("First element:", element)

# Negative indexing
last = my_tuple[-1]
print("Last element:", last)

# Slicing
sub_tuple = my_tuple[1:4]
print("Sliced tuple:", sub_tuple)

# Concatenate tuples
new_tuple = my_tuple + (6, 7, 8)
print("Concatenated:", new_tuple)

# Repeat tuple
repeated = my_tuple * 3
print("Repeated:", repeated)

# Unpack tuple
a, b, c = (1, 2, 3)
print(a, b, c)

# Unpack with *
a, *rest = (1, 2, 3, 4, 5)
print("a:", a, "rest:", rest)

# Swap values
a, b = 1, 2
a, b = b, a
print("Swapped:", a, b)

# Nested tuple
nested = ((1, 2), (3, 4))
print(nested)

# Count occurrences
count = my_tuple.count(2)
print("Count of 2:", count)

# Index of element
index = my_tuple.index(3)
print("Index of 3:", index)

# Membership check
exists = 3 in my_tuple
not_exists = 10 not in my_tuple
print("Exists 3:", exists, "Not exists 10:", not_exists)

# Tuple length, min, max, sum
print("Length:", len(my_tuple))
print("Max:", max(my_tuple))
print("Min:", min(my_tuple))
print("Sum:", sum(my_tuple))

# Sorting
sorted_tuple = sorted(my_tuple)
sorted_desc = sorted(my_tuple, reverse=True)
print("Sorted:", sorted_tuple)
print("Sorted desc:", sorted_desc)

# Convert list to tuple
tuple_from_list = tuple([1, 2, 3])
print(tuple_from_list)

# Convert string to tuple
tuple_from_string = tuple("Hello")
print(tuple_from_string)

# Zip tuples
zipped = tuple(zip((1, 2, 3), ('a', 'b', 'c')))
print(zipped)

# Enumerate tuple
for index, value in enumerate(my_tuple):
    print(index, value)

# Filter tuple
filtered = tuple(filter(lambda x: x % 2 == 0, my_tuple))
print("Filtered evens:", filtered)

# Map tuple
mapped = tuple(map(lambda x: x * 2, my_tuple))
print("Mapped (doubled):", mapped)

# Any / All
print("Any true:", any(my_tuple))
print("All true:", all(my_tuple))