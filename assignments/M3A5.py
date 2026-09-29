# Name: Isabella Romero
# Student ID: 865004683
# Section: 07
# Assignment: Module 3 Assignment 5

start_int = int(input("What is the first number? "))
end_int = int(input("What is the second number? "))

num_list = list(range(start_int, end_int + 1))
sum_int = 0

for number in num_list:
    if number % 5 == 0:
        sum_int = sum_int + number

print(f"The total value of multiples of {start_int} from {end_int} to {sum_int}")


