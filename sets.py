# Python Sets

print("\n--- Creating Sets ---")
my_set = {1, 2, 3, 4, 5}
print("Create a set:", my_set)

my_set2 = set([1, 2, 3, 4, 5])
print("Create set from list:", my_set2)

empty_set = set()
print("Empty set:", empty_set)

print("\n--- Adding / Updating ---")
my_set.add(6)
print("Add element 6:", my_set)

my_set.update([7, 8, 9])
print("Update with multiple elements [7,8,9]:", my_set)

print("\n--- Removing Elements ---")
my_set.remove(3)
print("Remove element 3:", my_set)

my_set.discard(10)  # no error if element not found
print("Discard element 10 (no error if missing):", my_set)

element = my_set.pop()
print("Pop random element:", element, "->", my_set)

my_set.clear()
print("Clear set:", my_set)

print("\n--- Copying ---")
my_set = {1, 2, 3, 4, 5}
new_set = my_set.copy()
print("Copy set:", new_set)

import copy
shallow_copy = copy.copy(my_set)
deep_copy = copy.deepcopy(my_set)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)

print("\n--- Set Operations ---")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
print("Union using union():", union_set)

union_set2 = set1 | set2
print("Union using | :", union_set2)

set1.update(set2)
print("Update set1 with union:", set1)

set1 = {1, 2, 3, 4}
intersect_set = set1.intersection(set2)
print("Intersection using intersection():", intersect_set)

intersect_set2 = set1 & set2
print("Intersection using & :", intersect_set2)

set1.intersection_update(set2)
print("Update set1 with intersection:", set1)

set1 = {1, 2, 3, 4}
diff_set = set1.difference(set2)
print("Difference set1 - set2:", diff_set)

diff_set2 = set1 - set2
print("Difference using - :", diff_set2)

set1.difference_update(set2)
print("Update set1 with difference:", set1)

set1 = {1, 2, 3, 4}
sym_diff = set1.symmetric_difference(set2)
print("Symmetric difference:", sym_diff)

sym_diff2 = set1 ^ set2
print("Symmetric difference using ^ :", sym_diff2)

set1.symmetric_difference_update(set2)
print("Update set1 with symmetric difference:", set1)

print("\n--- Subset / Superset Checks ---")
set1 = {1, 2}
set2 = {1, 2, 3, 4}

is_subset = set1.issubset(set2)
print("Check subset issubset:", is_subset)

is_subset2 = set1 <= set2
print("Check subset using <= :", is_subset2)

is_proper_subset = set1 < set2
print("Check proper subset using < :", is_proper_subset)

is_superset = set2.issuperset(set1)
print("Check superset issuperset:", is_superset)

is_superset2 = set2 >= set1
print("Check superset using >= :", is_superset2)

is_proper_superset = set2 > set1
print("Check proper superset using > :", is_proper_superset)

print("\n--- Disjoint Sets ---")
set3 = {7, 8, 9}
is_disjoint = set1.isdisjoint(set3)
print("Check if disjoint:", is_disjoint)

print("\n--- Frozen Sets (Immutable) ---")
frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)