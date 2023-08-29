#Autho: tz0feh
#Version 1.1
#Learning Python Programming
import random
print("Welcome to Dice Rolling in Python. Please choose your options below")
print(r"""       .-------.    ______
      /   o   /|   /\     \
     /_______/o|  /o \  o  \
     | o     | | /   o\_____\
     |   o   |o/ \o   /o    /
     |     o |/   \ o/  o  /
     '-------'     \/____o/
""")
def diceRoll():
    diceType = int(input("""Please choose your dice type (d4, d6, d8, d10, d12, d20, d100)
Type only the number: """))
    diceNum = int(input("How many dices?: "))

    print("Your dice rolling result for", str(diceNum)+"d"+str(diceType), "is:")
    for rolling in range(diceNum):
        print(random.randrange(1, diceType))
    repeat = input("Want to roll again? Press y to continue or any other to leave: ")
    if repeat.upper() == "Y":
        diceRoll()
    exit()
diceRoll()

##########################################################################################################################################################################

#Old Code
#A reminder that it can always be improved
#Author: tz0feh
#version: 1.0
#import random
#print("Welcome to Dice Rolling in Python. Please choose your options below")
#print(r"""       .-------.    ______
#      /   o   /|   /\     \
#     /_______/o|  /o \  o  \
#     | o     | | /   o\_____\
#     |   o   |o/ \o   /o    /
#     |     o |/   \ o/  o  /
#     '-------'     \/____o/
#""")
#def diceRoll():
#    diceType = input("Please choose your dice type (d4, d6, d8, d10, d12, d20, d100): ")
#
#    if diceType == "d4":
#        diceNum = int(input("How many dices?: "))
#        print("Your dice rolling result for", diceNum, diceType, "is:")
#        for rolling in range(diceNum):
#            print(random.randrange(1, 4))
#        repeat = input("Want to roll again? Press y to continue or any other leave: ")
#        if repeat.upper() == "Y":
#            diceRoll()
#        exit()
#
#    elif diceType == "d6":
#        diceNum = int(input("How many dices?: "))
#        print("Your dice rolling result for", diceNum, diceType, "is:")
#        for rolling in range(diceNum):
#            print(int(random.randrange(1, 6)))
#        repeat = input("Want to roll again? Press y to continue or any other leave: ")
#        if repeat.upper() == "Y":
#            diceRoll()
#        exit()
#
#    elif diceType == "d8":
#        diceNum = int(input("How many dices?: "))
#        print("Your dice rolling result for", diceNum, diceType, "is:")
#        for rolling in range(diceNum):
#            print(int(random.randrange(1, 8)))
#        repeat = input("Want to roll again? Press y to continue or any other leave: ")
#        if repeat.upper() == "Y":
#            diceRoll()
#        exit()
#
#    elif diceType == "d10":
#        diceNum = int(input("How many dices?: "))
#        print("Your dice rolling result for", diceNum,diceType, "is:")
#        for rolling in range(diceNum):
#            print(int(random.randrange(1, 10)))
#        repeat = input("Want to roll again? Press y to continue or any other leave: ")
#        if repeat.upper() == "Y":
#            diceRoll()
#        exit()
#
#    elif diceType == "d12":
#        diceNum = int(input("How many dices?: "))
#        print("Your dice rolling result for", diceNum, diceType, "is:")
#        for rolling in range(diceNum):
#            print(int(random.randrange(1, 12)))
#        repeat = input("Want to roll again? Press y to continue or any other leave: ")
#        if repeat.upper() == "Y":
#            diceRoll()
#        exit()
#
#    elif diceType == "d20":
#        diceNum = int(input("How many dices?: "))
#        print("Your dice rolling result for", diceNum, diceType, "is:")
#        for rolling in range(diceNum):
#            print(int(random.randrange(1, 20)))
#        repeat = input("Want to roll again? Press y to continue or any other leave: ")
#        if repeat.upper() == "Y":
#            diceRoll()
#        exit()
#
#    elif diceType == "d100":
#        diceNum = int(input("How many dices?: "))
#        print("Your dice rolling result for", diceNum, diceType, "is:")
#        for rolling in range(diceNum):
#            print(int(random.randrange(1, 100)))
#        repeat = input("Want to roll again? Press y to continue or any other leave: ")
#        if repeat.upper() == "Y":
#            diceRoll()
#        exit()
#
#    else:
#        print("Invalid Option")
#        diceRoll()
#
#diceRoll()
