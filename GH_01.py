#ASSIGMENT_01

students = {
    101: {"name": "Rahul", "branch": "CSE", "marks": 85},
    102: {"name": "Priya", "branch": "ECE", "marks": 90}
}


students[103] = {"name": "Aman", "branch": "ME", "marks": 78}


del students[102]
students[101]["marks"] = 88


student_tuple = (101, "Rahul", "CSE", 88)
student_list = [103, "Aman", "ME", 78]

print("Final Student Records:")
for roll_no, details in students.items():
    print(roll_no, details)


#ASSIGMENT_02
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


#ASSIGMENT_03
def check_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("It is a right-angled triangle.")
    else:
        print("It is not a right-angled triangle.")

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

check_right_triangle(a, b, c)

#ASSIGMENT_04
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

new = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        new[i][j] = matrix1[i][j] + matrix2[i][j]

print("Addition of two matrices:")
for row in new:
    print(row)

#ASSIGMENT_05
import re

pan = input("Enter PAN number: ")

pattern = "^[A-Z]{5}[0-9]{4}[A-Z]$"

if re.match(pattern, pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")























