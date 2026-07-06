# 1. Age Calculator
# Input age.
# Print:
# Your age after 10 years:
age = int(input("Enter your age: "))
print("Your age after 10 years:", age + 10)

# 2. Rectangle Area
# Input:
# •	length 
# •	width 
# Print area.
length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
area = length * width
print("Area of rectangle is:", area)

# 3. Even Odd Checker
# Hint:
# %
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

# 4. Marks Percentage
# Input:
# •	total 
# •	obtained 
# Calculate percentage.
input_total = float(input("Enter total marks: "))
input_obtained = float(input("Enter obtained marks: "))
percentage = (input_obtained / input_total) * 100
print("Percentage:", percentage, "%")


# 5. Salary Increment
# Input salary.
# Increase by 10%.
salary = float(input("Enter your current salary: "))
increment_salary = salary * 0.10
new_salary = salary + increment_salary
print("Your salary after 10% increment will be:", new_salary)



