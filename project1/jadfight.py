#!/usr/bin/env python3

import random
import time
import datetime
import sys, select

round = 0+1 
player_dam = 10
jad_health = 100
jad_type = ["ranged", "mage", "melee"] #defines Jad's 3 attack styles
jad_attack = random.choice(jad_type) #randomly chooses between the 3 attack styles
jad_dam= (random.randint(55,90)) #rolls random damage number between 55 and 90

##Tells the player which attack Jad is using
#jad_attack
if jad_attack == jad_type[0]:
    print("Jad rears back and SLAMS his fists on the ground")
elif jad_attack == jad_type[1]:
    print("Jad leans back and CASTS METEOR at your location")
elif jad_attack == jad_type[2]:
    print("Jad readies his FISTS to pummel you")

##Gives the player 5 seconds to choose their prayer
print("you have five seconds to choose your prayer")

i, o, e = select.select([sys.stdin],[],[], 5 )


if (i) and sys.stdin.readline().strip() == jad_type[0] and jad_attack == jad_type[0]:
    print("you avoided the damage!")
elif (i) and sys.stdin.readline().strip() == jad_type[1] and jad_attack == jad_type[1]:
    print("you avoided the damage!")
elif (i) and sys.stdin.readline().strip() == jad_type[2] and jad_attack == jad_type[2]:
    print("you avoided the damage!")
else:
    print ("you took", jad_dam, "damage!")


##prayer = input("Quick choose your prayer!\n") #request prayer choice from player
##time.sleep(2) #sleep for 2 seconds
##print("you activated protect from", prayer) #displays the input back to the player
##time.sleep(2) #sleep for 2 seconds
##print("Jad attacked with", jad_attack) #displays which style Jad decided to attack with
##time.sleep(2) #sleep for 2 seconds


##if jad_attack == prayer:
  ## print("You avoided the damage!") 
##else:
    ##print("Oh no! Jad hit you for", jad_dam, "damage!")



