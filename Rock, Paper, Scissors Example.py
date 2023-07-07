#create a list of play options
from random import randint


t = ["KFC", "Popeyes", "Zaxbys"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
    #set player to True
    player = input("KFC, Popeyes, Zaxbys?")
    if player == computer:
        print("Tie!")
    elif player == "KFC":
        if computer == "Popeyes":
            print("You lose!", computer, "covers, player")
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Popeyes":
        if computer == "Zaxybs":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Zaxbys":
        if computer == "KFC":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
    
