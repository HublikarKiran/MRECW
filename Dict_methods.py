
# Python Dictionaries Methods


from collections import OrderedDict
import copy
print("\n--- Creating Dictionaries ---")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Create dictionary:", my_dict)

my_dict2 = dict(a=1, b=2, c=3)
print("Create with dict() constructor:", my_dict2)

my_dict3 = dict([('a', 1), ('b', 2), ('c', 3)])
print("Create from list of tuples:", my_dict3)

print("\n--- Accessing Values ---")
value = my_dict['a']
print("Access value by key ['a']:", value)

value = my_dict.get('d', 0)
print("Get value with default (key 'd'):", value)

print("\n--- Adding / Updating ---")
my_dict['d'] = 4
print("Add/update item d=4:", my_dict)

my_dict.update({'e': 5, 'f': 6})
print("Update multiple items:", my_dict)

print("\n--- Removing Items ---")
del my_dict['b']
print("Remove item with del ['b']:", my_dict)

val = my_dict.pop('c')
print("Pop item ['c']:", val, "->", my_dict)

val2 = my_dict.pop('e', None)
print("Pop with default (e):", val2, "->", my_dict)

item = my_dict.popitem()
print("Remove and return last item:", item, "->", my_dict)

my_dict.clear()
print("Clear dictionary:", my_dict)

print("\n--- Keys, Values, Items ---")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Reset dict:", my_dict)

keys = my_dict.keys()
print("Keys:", keys)

values = my_dict.values()
print("Values:", values)

items = my_dict.items()
print("Items:", items)

print("\n--- Copying ---")
new_dict = my_dict.copy()
print("Shallow copy using copy():", new_dict)

shallow_copy = copy.copy(my_dict)
deep_copy = copy.deepcopy(my_dict)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)

print("\n--- Membership Tests ---")
exists = 'a' in my_dict
print("'a' exists:", exists)

not_exists = 'z' not in my_dict
print("'z' not exists:", not_exists)

print("\n--- Dictionary Comprehensions ---")
squared = {x: x**2 for x in range(5)}
print("Squared values:", squared)

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even squares (conditional):", even_squares)

print("\n--- Merging Dictionaries ---")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged1 = dict1 | dict2   # Python 3.9+
print("Merged (| operator, 3.9+):", merged1)

merged2 = {**dict1, **dict2}  # Python 3.5+
print("Merged (** unpacking, 3.5+):", merged2)

print("\n--- Other Useful Methods ---")
length = len(my_dict)
print("Length of dict:", length)

new_dict2 = dict.fromkeys(['a', 'b', 'c'], 0)
print("Create dict with default values:", new_dict2)

my_dict = {'a': 1, 'b': 2}
val = my_dict.setdefault('c', 5)
print("Set default for missing key 'c':", val, "->", my_dict)

val2 = my_dict.setdefault('b', 10)
print("Set default for existing key 'b':", val2, "->", my_dict)

ordered = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print("OrderedDict:", ordered)
