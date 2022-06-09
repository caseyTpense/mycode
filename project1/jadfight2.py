import threading
import os
import random
import time


player= [99, 25] #player starts with 99 health points and their attack does 25 damage
jad= [100, 55] #Jad starts with 100 health and his attack does 55 damage
jad_type = ["ranged", "mage", "melee"] #defines Jad's 3 attack styles
##jad_attack = (random.choice(jad_type)) #randomly chooses between the 3 attack styles

weapon= input("Choose your weapon: crossbow, blowpipe, or twisted bow\n")

def damage():
    print("you took", jad[1], "damage!")
    player[0] = player[0] - jad[1]
    print("your Health points are now", player[0])


##def fight_seq():
    #tells jad to attack
while player[0] > 0 and jad[0] > 0: 
    ##Gives the player 5 seconds to choose their prayer
    print("you have five seconds to choose your prayer")
    pt = threading.Timer(5.0, damage) #creates a timer to choose prayer or else be damaged
    pt.start() #starts the timer thread
    #Tells the player which attack Jad is using

    random.choice(jad_type)
    if random.choice(jad_type) == jad_type[0]:
        print("Jad rears back and SLAMS his fists on the ground")
    elif random.choice(jad_type) == jad_type[1]:
        print("Jad leans back and CASTS METEOR at your location")
    elif random.choice(jad_type) == jad_type[2]:
        print("Jad readies his FISTS to pummel you")
    else:
        random.choice(jad_type)

    prayer= input("Quick choose your prayer!\n")

    if random.choice(jad_type) == jad_type[0] and prayer == jad_type[0]:
        print("Jad's ranged attack did no damage!")
        time.sleep(1)
        print("You shoot your", weapon, "and deal", player[1], "damage to Jad!")
        time.sleep(1)
        jad[0] = jad[0] - player[1]
        print("Jad has", jad[0], "health remaining")
        time.sleep(1)
    elif random.choice(jad_type) == jad_type[1] and prayer == jad_type[1]:
        print("Jad's mage attack did no damage!")
        time.sleep(1)
        print("You shoot your", weapon, "and deal", player[1], "damage to Jad!")
        time.sleep(1)
        jad[0] = jad[0] - player[1]
        print("Jad has", jad[0], "health remaining")
        time.sleep(1)
    elif random.choice(jad_type) == jad_type[2] and prayer == jad_type[2]:
        print("Jad's melee attack did no damage!")
        time.sleep(1)
        print("You shoot your", weapon, "and deal", player[1], "damage to Jad!")
        time.sleep(1)
        jad[0]= jad[0]- player[1]
        print("Jad has", jad[0], "health remaining")
        time.sleep(1)
    else:
        damage
    pt.cancel()
   
    if player[0] <= 0:
        print("Jad slapped you, go train on some rock crabs and come back ya nub")
        break
    if jad[0] <= 0:
        print("The entire cave shakes as Jad falls dead to the floor. Claim your fire cape from the Tzhaar outside")
        print("Congrats you won!")
        break
    
