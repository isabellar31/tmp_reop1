# Name: Isabella Romero
# Student ID: 865004683
# Section: 07
# Assignment: Module 4 Assignment 1

g_list = []

for number in range(1, 4):
    game = input(f"What is your number {number} favorite PlayStation game? ")
    g_list.append(game)

for number, game in enumerate(g_list, start=1):
    print(f"Your number {number} favorite game was {game}")


