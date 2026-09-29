# Name: Isabella Romero
# Student ID: 865004683
# Section: 07
# Assignment: Module 4 Assignment 2

food_dict = {}

for number in range(3):
    food = input("What is good to eat? ")
    country = input("What country is that from? ")
    food_dict[food] = country


dish = input("What dish do you like? ")
print(f"{dish} is from {food_dict[dish]}")