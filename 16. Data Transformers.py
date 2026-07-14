# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  Complete the following tasks:

# Use map() to create a new list containing the square of every number.
# Use filter() to create a list containing only the even numbers.
# Use filter() to create a list containing only numbers greater than 5.
# Use reduce() to calculate the sum of all numbers.
# Use reduce() to find the largest number in the list.
# Combine map() and filter():
# First, square every number.
# Then, keep only the squared values greater than 20.

from functools import reduce

# Square every number with map()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print("Numbers > 5:", greater_than_5)

# Sum of all numbers with reduce()
total_sum = reduce(lambda a, b: a + b, numbers)
print("Sum:", total_sum)

# Largest number with reduce()
largest = reduce(lambda a,b: a if a>b else b, numbers)
print("Largest:", largest)

# Combine map() and filter()
squared_filtered = list(filter(lambda x: x>20, map(lambda x: x**2, numbers)))
print("Squares > 20:", squared_filtered)

