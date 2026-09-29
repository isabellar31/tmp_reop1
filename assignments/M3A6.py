# Name: Isabella Romero
# Student ID: 865004683
# Section: 07
# Assignment: Module 3 Assignment 6

student_name = input("What is the student name? ")
score = int(input("What is their score? "))

if score >= 90:
    letter_grade = "A"
elif score >= 80:
    letter_grade = "B"
elif score >= 70:
    letter_grade = "C"
elif score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"{student_name} earned a {letter_grade}")
