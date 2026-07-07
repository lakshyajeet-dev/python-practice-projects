# Create list of 5 numbers and print largest. 
numbers = [10, 25, 7, 42, 18]   # Create a list with 5 numbers
print("Largest number:", max(numbers))  # max() finds the biggest value

# Take 5 inputs and store in list. 
nums = []
for i in range(5):
    n = int(input("Enter a number: "))
    nums.append(n)
print("Your list:", nums)

# Reverse a list without reverse(). 
numbers = [1, 2, 3, 4, 5, 6]
reversed_list = numbers[::-1]
print("Reversed list: ", reversed_list)


# Count even numbers. 
numbers = [2, 5, 8, 11, 14]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print("Even numbers count:", count)    

# Remove duplicates. 
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = []
for n in nums:
    if n not in unique_nums:
        unique_nums.append(n)
print("List without duplicate: ", unique_nums)    

# Find second largest. 
numbers = [10, 25, 7, 42, 18]
numbers.sort()    # Sort the list in ascending order
second_largest = numbers[-2]   # get the second last element
print("Second largest number: ", second_largest)


# Merge two lists. 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("Merged list: ", merged)

# Create multiplication table using list comprehension. 
num = 5
table = [num * i for i in range(1, 11)]  # Generate list of products
print(f"Table of {num}:", table)

# Store marks and calculate average. 
marks = [85, 90, 78, 92, 88]
average = sum(marks) / len(marks)
print("Average:", average)

# •  Find common elements in two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = [element for element in list1 if element in list2]
print("Common elements:", common)