#!/usr/bin/python3

#imports 
import random
import time
import os


## A dictionary linking a room to other rooms
rooms = {

            'Living Quarters' : {
                  'west' : 'Northern Corridor',
                  
                  'item'  : 'key'
                },
            'Northern Corridor' : {
                    'north' : 'Main Deck',
                    'south' : 'Central Corridor',
                    'east'  : 'Living Quarters',
                    'west'  : 'Kitchen',
                    'item'  : 'monster',
                 },

            'Central Corridor' : {
                  'north' : 'Northern Corridor',
                  'south' : 'Southern Corridor',
                  'east'  : 'Mission Control',
                  'west'  : 'Medical',
                  'item'  : 'monster',
                },
            'Southern Corridor' : {
                   'north' : 'Central Corridor',
                   'south' : 'Cargo Bay',
                   'east'  : 'Escape Pod',
                   'west': 'Engineering Bay',
                   'item'  : 'monster',
                 },
            'Mission Control' : {
                    'west'  : 'Central Corridor',
                    'item'  : 'monster',
                 },
            'Medical' : {
                    'east'  : 'Central Corridor',
                    'item'  : 'monster',
                 },
            'Kitchen' : {
                  'east' : 'Northern Corridor',
                  'item' : 'potion',
               },
            'Engineering Bay' : {
                    'south' : 'Cargo Bay',
                    'east'  : 'Southern Corridor',
                    'west'  : 'Kitchen',
                    'item'  : 'monster',
                 },
            'Escape Pod' : {
                  'west' : 'Southern Corridor',
               },
            'Main Deck' : {
                  'south' : 'Northern Corridor',
                  'item' : 'cookie',
            },
            'Cargo Bay' : {
                    'north west' : 'Engineering Bay',
                    'north' : 'Southern Corridor',
                    'item'  : 'monster',
                 },
         }

## A dictionary defining alien types, attributes, and spells
aliens = {
            'Phlorpian Grunt' : {
                 'attack' : random.randint(0, 5),
                 'health' : int(10),
                },
            'Phlorpian Initiate' : {
                 'attack' : random.randint(0, 10),
                 'health' : int(15),
                 },
            'Phlorpian Zealot' : {
                'attack' : random.randint(0, 10),
                'health' : int(30),
                'lesser heal' : int(5),
                },
            'Phlorpian Brute' : {
                'attack' : random.randint(0, 20),
                'health' : int(55),
                },
            'Phlorpian Berserker' : {
                'attack' : random.randint(5,55),
                'health' : int(5)
                },
            'Fad Cheeser' : {
                'attack' : random.randint (0,25),
                'health' : int(75),
                'lesser heal'   : random.randint (0,5),
                'Holy Fire' : random.randint (0, 40),
                },
        }

player = {
            'health' : int(50),
            'attack' : random.randint(0,5),
            }    

    
# print("Prepare yourself, a fight is imminent!")
# time.sleep(1)
#def combat():
#    while player['health'] > 0 and aliens['Phlorpian Grunt']['health'] > 0
#        for enemy in aliens:
#        print("the ". enemy, "is ready to battle!")

#       combat choice = input('Do you want to strike or attempt to flee?')
#       if combat choice == 'strike':


        

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []



#start the player in the Hall
currentRoom = 'Living Quarters'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  if move[0] == 'use' :
      #if item in inventory and item is the one they want to use
    item_to_use= input('which item would you like to use? WARNING: The item will be consumed on use\n')
    if item_to_use in inventory:
        print("you used", item_to_use, "\n")
        inventory.remove(item_to_use)
    else:
    #tell them they dont have that item
        print('you do not have that item\n')



  ## Define how a player can win
#  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
#    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
#    break

  ## If a player enters a room with a monster
#    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
#    print('A monster has got you... GAME OVER!')
#    break
