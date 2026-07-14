# Write a Python program that:

# Creates two separate lists with the same values and compares them using both == and is.
# Creates a third variable that references the first list and compares it using both operators.
# Modifies the third variable and observes how it affects the first list.
# Prints a short explanation (using comments) describing why the outputs are different.

# Identity vs Equality Practice

# Create two separate lists with the same values
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 == list1:", list1 == list2) # True because values are equal
print("list1 is list2:", list1 is list2) # False because they are different objects

# Create a third variable referencing the first list
list3 = list1
print("list1 == list3:", list1 == list3)   # True because values are equal
print("list1 is list3:", list1 is list3)   # True because both point to same object

# Modify the third variable
list3.append(4)

print("list1 after modifying list3:", list1)  # list1 also changes
print("list3:", list3)

# Explanation:
# == checks if values inside are the same.
# is checks if both variables point to the same object in memory.
# list1 and list2 have equal values but are stored separately → == True, is False.
# list3 references list1 → both point to same object → == True, is True.
# Changing list3 also changes list1 because they are the same object.