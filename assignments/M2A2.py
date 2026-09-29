# Name: Isabella Romero
# Student ID: 865004683
# Section: 07
# Assignment: Module 2 Assignment 2

g_list = ['Mortal Kombat', 'Contra', 'Streets Of Rage', 'Shinobi', 'Sonic', 'Phantasy Star']
print("Here are the top Sega games:")
for game in g_list:
    print(game)

g_removed = input("Which one do you think should be removed? ")
g_list.remove(g_removed)

print("Here are the new top Sega games:")
for game in g_list:
    print(game)


