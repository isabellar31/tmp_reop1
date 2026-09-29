# Name: Isabella Romero
# Student ID: 865004683
# Section: 07
# Assignment: Module 3 Assignment 4

current_year = int(input("What year is it now? "))
birth_year = int(input("What year were you born? "))

age_int = current_year - birth_year

if age_int < 50 and age_int % 2 == 0:
    print("This will be a great year")
elif age_int < 50 and age_int % 2 == 1:
    print("This year will be tough")
elif age_int == 50:
    print("The future is unclear")
elif age_int > 50:
    print("Death will come for you soon")

