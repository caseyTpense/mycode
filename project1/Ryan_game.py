#!/usr/bin/env python3


username = input("What is your name, Tarnished?\n>")

print("Nice to meet you ", username, ". Your adventure may now begin.\nFor now you should rest....\n")
input("---Your eyes feel heavy and your body begin to tire...\nYou cannot help but fall asleep....\n")

tarnished_stats = {
    "attack":15,
    "health":20,
    "weapon":"sword",
    "class":"warrior",
    }
tree_sentinel = {
    "attack":12,
    "health":30,
    "weapon":"axe",
    }

#health_status = int(tarnished_stats["health"])
#enemy_health = int(tree_sentinel["health"])
#enemy_attack = int(tree_sentinel["attack"])
#tarnished_attack = int(tarnished_stats["attack"])
#tarnished_stats["health"] = health_status - enemy_attack
#tree_sentinel["health"] = enemy_health - tarnished_attack

    

directions= ["Left", "Right", "Back", "Forward"]
yes_no= ["Yes", "No"]
dodge_attack= ["Dodge", "Attack"]

def combat():
    input("You encountered a tree sentinel!")
    response = ""
    while response not in yes_no:
        response = input("Would you like to attack the tree sentinel? Yes or No?\n>").title()
        if response == 'Yes':
            print("You approach the sentinel and you attack with your sword!")
            tree_sentinel["health"] = tree_sentinel["health"] - tarnished_stats["attack"]
            print("The sentinel's health has decreased from 30 to ", tree_sentinel["health"], "!\n" )
        elif response == 'No':
            print("You are a coward.\nGame over.\n")
            quit()
        else:
            print("I did not understand that. You have to be precise.\n")
            
#def combat_round():
    input("The tree sentinel did not like what you did.\nHe's about to attack!")
      
    response = ""
    while response not in dodge_attack:
        response = input("Do you want to dodge or attack?").title()
        if response == 'Dodge':
            print("You were too slow! The sentinel has gashed you with his axe damaging you ", tree_sentinel["attack"], " points!\n")
            tarnished_stats["health"] = tarnished_stats["health"] - tree_sentinel["attack"]
            print("Your health is now ", tarnished_stats["health"], "!\n")
        elif response == 'Attack':
            print("You were too slow! The sentinel has gashed you with his axe damaging you ", tree_sentinel["attack"], " points!\n")
            tarnished_stats["health"] = tarnished_stats["health"] - tree_sentinel["attack"]
            print("Your health is now ", tarnished_stats["health"], "!\n")
        else:
            print("heh? what was that again?\n")
  
    response = ""
    while response not in yes_no:
          response = input("Let's try and attack again! Now is our chance! Do you want to?").title()
          if response == 'Yes':
              print("You attacked him with your sword, you inflicted damage!\n")
              tree_sentinel["health"] = tree_sentinel["health"] - tarnished_stats["attack"]  
              
          elif response == 'No':
              print("Wow what a loser.")
              quit()
          else:
              print("huh?")


response = ""
while response not in yes_no:

    response= input("You wake up from your deep sleep and you find yourself in a dark cave.\nAhead of you is a light at the end of the tunnel. Would you like to proceed?\n>").title()
    if response == 'Yes':
        print("You walk towards the light at the end of the tunnel. You find that it is an exit out of the cave.\n")
    elif response == 'No':
        print("This cave is empty. There are no items and there are no other pathways.\n")
    else:
        print("I did not understand that")


input("You exit the cave and what lies before you is the land they call...\n")

input("The Lands Between.\n")

input("In front of you is a man with a white mask.\nTo your left is the forest.\nTo your right is the forest.\nBehind you is the cave.\n")

input("To be honest I don't know why it feels like I am giving you options...\nWhen really....I am not.\n")

response = ""
while response not in yes_no:
    response = input("Would you like to talk to the man with the white mask?\n>").title()
    if response == 'Yes':
        print("The white mask man opens his mouth to speak....\n")
    elif response == 'No':
        print("Are you scared or something? Go and talk to him.\n")
    else:
        print("I only understand yes or no answers.\n")

input("You lean in closer to hear his words....")

input("He kills you.\n")

input("He proceeds to teabag you...\n")

input("....and he called you maidenless.\n")

response = ""
while response not in yes_no:
    response = input("Would you like to continue?\n>").title()
    if response == 'Yes':
        print("You wake up in the cave and exit out.\n")
    elif response == 'No':
        print("Wow. What a quitter.\n")
        print("Game over.")
        quit()
    else:
        print("Yes or no answers only.\n")

input("Sorry for forcing you to talk to the white mask man.\n")
print("To your right is the forest.\nTo your left is the forest.\nBehind you is the cave.\nAnd of course, in front of you is the white mask man.\n")


#Enough playing around. Time to play around.

response = ""
while response not in directions:
    response = input("Where would you like to go? Right, left, back, or forward?\n>").title()
    if response == 'Forward':
        print("Don't let the white mask man disrespect you again. Kill him.\n")
    elif response == 'Right':
        print("You walk towards the forest to your right.\n")
        combat()

      
    elif response == 'Left':
        print("You walk towards the forest to your left.\n")
    elif response == 'Back':
        print("You step back into the cave.\n")
    else:
        print("I only understand directional answers.\n")
if tarnished_stats["health"] <= 0:
    print("You Died")
    quit()

if tree_sentinel["health"] <= 0:
    print("The tree sentinel has died!")
    print("We did it! We did it! We wonnn!\n")
    print("Thank you for playing!")
while tree_sentinel["health"] > 0 or tarnished_stats["health"] <= 0:
  #combat_round()
  combat()
