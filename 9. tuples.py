# Project 1 — Student Record
# Store:
# •	name 
# •	age 
# •	marks 
# using tuple.
# Student Record using tuple
student = ("Lakshyajeet", 20, 85)   # Tuple stores name, age, marks

print("Name:", student[0])          # Access first element
print("Age:", student[1])           # Access second element
print("Marks:", student[2])         # Access third element


# Project 2 — Coordinate Distance
# Store points.
import math
point1 = (2, 3)
point2 = (7, 8)
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
print("Distance between points:", distance)

# Project 3 — Quiz Result
# Return multiple values from function.
def quiz_result(correct, total):
    percentage = correct / total * 100
    if percentage >= 75:
        grade = "Pass"
    else:
        grade = "Fail"
    return percentage, grade
score = quiz_result(18, 20)
print("Percentage:", score[0])
print("Result:", score[1])
    

