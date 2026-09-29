# Name: Isabella Romero
# Student ID: 865004683
# Section: 07
# Assignment: Module 4 Assignment 3

games_dict = {}

for game in range(3):
    game = input("What is a great game? ")
    system = input("What system can I play that on? ")
    games_dict[game] = system

print("That's too many, let's get rid of one")

game_del = input("What game should we remove? ")

del games_dict[game_del]

print("The new dictionary is:")

for game, system in games_dict.items():
    print(f"You can play {game} on {system}")


