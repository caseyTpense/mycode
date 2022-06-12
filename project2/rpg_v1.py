#!/usr/bin/python3G

#imports 
import random
import time
import os


## A dictionary defining alien types, attributes, and spells
aliens = {
            'Phlorpian Grunt' : {
                 'health' : int(10),
                },
            'Phlorpian Initiate' : {
                 'health' : int(15),
                 },
            'Phlorpian Zealot' : {
                'health' : int(30),
                'lesser heal' : int(5),
                },
            'Phlorpian Brute' : {
                'health' : int(55),
                },
            'Phlorpian Berserker' : {
                'health' : int(10),
                },
            'Fad Cheeser' : {
                'health' : int(75),
                'moderate heal'   : random.randint (0,10),
                'Holy Fire' : 'random.randint (0, 40)',
                },
        }

## A dictionary linking a room to other rooms
rooms = {

            'Living Quarters' : {
                  'west' : 'Northern Corridor',
                  'item'  : 'dads lucky charm',
                  'hello' : "Chad",
                },
            'Northern Corridor' : {
                        'north' : 'Main Deck',
                        'south' : 'Central Corridor',
                        'east'  : 'Living Quarters',
                        'west'  : 'Kitchen',
                        'item'  : '', 
                        'monster' :'Phlorpian Grunt',
                        'alien' : aliens['Phlorpian Grunt'],
                 },

            'Central Corridor' : {
                  'north' : 'Northern Corridor',
                  'south' : 'Southern Corridor',
                  'east'  : 'Mission Control',
                  'west'  : 'Medical',
                  'item'  : '',
                },
            'Southern Corridor' : {
                   'north' : 'Central Corridor',
                   'south' : 'Cargo Bay',
                   'east'  : 'Escape Pod',
                   'west'  : 'Engineering Bay',
                   'item'  : '',
                'monster'  : 'Phlorpian Brute'
                 },
            'Mission Control' : {
                    'west'  : 'Central Corridor',
                    'item'  : '',
                 },
            'Medical' : {
                    'east'  : 'Central Corridor',
                    'item'  : 'health potion',
                 },
            'Kitchen' : {
                'east'   : 'Northern Corridor',
                'item'   : 'health potion',
                'monster': 'Phlorpian Initiate'
               },
            'Engineering Bay' : {
                    'south' : 'Cargo Bay',
                    'east'  : 'Southern Corridor',
                    'west'  : 'Kitchen',
                     
                 },
            'Escape Pod'    : {
                  'west'    : 'Southern Corridor',
                  'monster' : 'Fad Cheeser',
               },
            'Main Deck' : {
                  'south' : 'Northern Corridor',
                  'item'  : 'cookie',
                'monster' : 'Phlorpian Zealot',
            },
            'Cargo Bay' : {
               'north west' : 'Engineering Bay',
                'north'     : 'Southern Corridor',
                'item'      : '',
                'monster'   : 'Phlorpian Berserker',
                 },
         }


player_dam = list(range(0, 6))
## A dictionary defining alien types, attributes, and spells
player = {
            'health' : int(50),
            }    

chad_feeser = {
            'health' : int(1),
    }
    

escape_chance = ['successful','unsuccessful']
spell_or_attack = ['attack','spell']
which_spell = ['holy fire', 'moderate heal']

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use (press enter to choose item from inventory)
  drop (press enter to choose item from inventory)
''')

#start the player in the Living Quarters
currentRoom = 'Living Quarters'
currentAlien = ''
showInstructions()
# print("Prepare yourself, a fight is imminent!")
# time.sleep(1)
#def combat():
#    while player['health'] > 0 and aliens['Phlorpian Grunt']['health'] > 0
#        for enemy in aliens:
#        print("the ". enemy, "is ready to battle!")

#       combat choice = input('Do you want to strike or attempt to flee?')
#       if combat choice == 'strike':



def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if 'item' in rooms[currentRoom]:
    print('You see a', rooms[currentRoom]['item'])
  else:
      print('There seems to be nothing of interest left in this room')
  print("---------------------------")            
#an inventory, which is initially empty
inventory = []

    

#loop forever
while True:

  showStatus()
  if currentRoom == 'Living Quarters' and 'dads lucky charm' not in inventory:
    print('Chad Feeser says: "Hey whats your name again?"')
    player_name= input()
    if player_name.lower()  == 'chad':
        print('Chad: "Oh yeah? well too bad because theres only room for one Chad on this ship!"\nChad pulls out his blaster and blows a hole through your skull\n... Damn I guess get good...')
    else:
        print('Chad: "yeah well,', player_name, 'get the hell up something crazy is happening and Im not sure what it is."\n"Lead the way', player_name, 'Oh, and dont forget your little good luck charm there on your table. Youre probably gonna need all the luck you can get. "\n')

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
  #if they type 'use' first
  if move[0] == 'use' :
      #if item in inventory and item is the one they want to use
    item_to_use= input('which item would you like to use? WARNING: The item will be consumed on use\n')
    use_choice= input('WARNING: '+ item_to_use + ' will be consumed on use. Are you sure you want to use it? (yes or no)\n')
    #user decides to use the item and they have the item
    if use_choice.lower()== 'yes' and item_to_use.lower() in inventory:
        print('you used', item_to_use, '\n')
        inventory.remove(item_to_use)
        if item_to_use == 'scroll of glokin':
            player['health'] = player['health'] + 100
            print('You gained 100 health points and now have', player['health'], 'health points!')
        elif item_to_use == 'guts':
            print('ew..what? why woudld you.... mmk well now you just smell bad I guess')
        elif item_to_use == 'health potion':
            player['health'] = player['health'] + 40
            print('You gained 40 health points and now have', player['health'], 'health points!')
        #player decides not to use the item
    elif use_choice.lower()== 'no':
        print('you leave', item_to_use, 'in your inventory.')
        #tell them they dont have that item
    elif item_to_use.lower() not in inventory:
        print('you do not have that item in your inventory.')    
    else:
        print('make another choice')
 #if they type 'drop' first
  if move[0] == 'drop' :
      #ask for which item they want to drop and warn what will happen to dropped item
    item_to_drop= input('which item would you like to drop?\n')
    drop_choice= input('WARNING: ' + item_to_drop + ' will be dropped to the ground. Are you sure you want to drop it? You can pick it up again. (yes or no)\n')
        #if they have the item and want to drop it, removes item from inventory and adds the item to the current room's item key in room dict             and shows the new status
    if drop_choice.lower()== 'yes' and item_to_drop.lower() in inventory:
        print("you dropped", item_to_drop, "to the floor.\n")
        inventory.remove(item_to_drop)
        rooms[currentRoom]['item'] = item_to_drop
        # if player says no to dropping the item tell them nothing happened
    elif use_choice.lower()== 'no':
        print('you leave', item_to_drop, 'in your inventory.')
        #if you dont have the item you wanted to drop then notify
    elif item_to_drop.lower() not in inventory:
        print('you do not have that item in your inventory.')
    else:
        #retry
        print('try again\n')
 

 ##spawn condition for monsters       
  if 'monster' in rooms[currentRoom] and 'dads lucky charm' in inventory:
        showStatus()
        print('There is a', rooms[currentRoom]['monster'], 'prepared to fight!')
        time.sleep(3)
    

        
        while player['health'] > 0 and aliens['Phlorpian Grunt']['health'] > 0: #fight till somethin dies
            combat_choice = input('Do you want to fight or escape?') # input choice to fight or attempt escape
            if combat_choice == 'fight': # if fight, combat starts
                player_damage= random.randint(0,5) #damage for player 
                #hp reduction for monster based on player attack
                aliens['Phlorpian Grunt']['health'] = aliens['Phlorpian Grunt']['health'] - player_damage 
                print('you use your blaster to damage the Phlorpian Grunt for', player_damage, 'the Phlorpian Grunt has', aliens['Phlorpian Grunt']['health'], 'health remaining\n---------------------------' )                   
                time.sleep(1.5) #gives scroll time
                alien_damage = random.randint(0,5) #damage for monster
                player['health'] = player['health'] - alien_damage # reduction of player health based on monster attack
                print('The Phlorpian Grunt slaps you with his crongelon for', alien_damage, 'you have', player['health'], 'health remaining.\n ---------------------------')
            
##escape option if statements 
            elif combat_choice == 'escape':
                escape_outcome = random.choice(escape_chance) #rolls to see if you can escape

                if escape_outcome == 'successful': 
                    currentRoom = random.choice(list(rooms.keys())) #if you escape puts you in a random room on the spaceship
                    print('you escaped successfully to', currentRoom, "! That was a close one.")
                    break
                elif escape_outcome == 'unsuccessful': #take damage if you roll unsuccessful escape
                    alien_damage = random.randint(0,5)
                    player['health'] = player['health'] - alien_damage
                    print('You failed to escape and the Phlorpian Grunt hit you for', alien_damage, 'you have', player['health'], 'health remaining.')
                
            else: #what happens if you put anything other than escape or attack
                print('It looks like you only have 2 options in this predicament that you have found yourself in. please choose fight or escape.') 
            
            if aliens['Phlorpian Grunt']['health'] <= 0: #ends combat 
                print('Good job! That Phlorpian Grunt didnt stand a chance! You see the Phlorpian Grunts crongelon on the ground. Maybe you could use it to upgrade your blaster.')
                del rooms[currentRoom]['monster'] # removes the rooms monste
                rooms[currentRoom]['item'] = 'crongelon' #drops item in room
                break                 


  if 'monster' in rooms[currentRoom] and 'dads lucky charm' in inventory:
        while player['health'] > 0 and aliens['Phlorpian Initiate']['health'] > 0: #fight till somethin dies
                combat_choice = input('Do you want to fight or escape?') # input choice to fight or attempt escape
                if combat_choice == 'fight': # if fight, combat starts
                    player_damage= random.randint(0,10) #damage for player 
                #hp reduction for monster based on player attack
                    aliens['Phlorpian Initiate']['health'] = aliens['Phlorpian Initiate']['health'] - player_damage
                    print('you use your blaster to damage the Phlorpian Initiate for', player_damage, 'the Phlorpian Initiate has', aliens['Phlorpian Initiate']['health'], 'health remaining\n---------------------------' )
                    time.sleep(1.5) #gives scroll time
                    alien_damage = random.randint(0,10) #damage for monster
                    player['health'] = player['health'] - alien_damage # reduction of player health based on monster attack
                    print('The Phlorpian Initiate blasts you with his phase zinger for', alien_damage, 'you have', player['health'], 'health remaining.\n ---------------------------')

##escape option if statements 
                elif combat_choice == 'escape':
                    escape_outcome = random.choice(escape_chance) #rolls to see if you can escape

                    if escape_outcome == 'successful':
                        currentRoom = random.choice(list(rooms.keys())) #if you escape puts you in a random room on the spaceship
                        print('you escaped successfully to', currentRoom, "! That was a close one.")
                        break
                    elif escape_outcome == 'unsuccessful': #take damage if you roll unsuccessful escape
                        alien_damage = random.randint(0,5)
                        player['health'] = player['health'] - alien_damage
                        print('You failed to escape and the Phlorpian Initiate hit you for', alien_damage, 'you have', player['health'], 'health remaining.')

                else: #what happens if you put anything other than escape or attack
                    print('It looks like you only have 2 options in this predicament that you have found yourself in. please choose fight or escape.')

                if aliens['Phlorpian Initiate']['health'] <= 0: #ends combat 
                    print('Good job! That Phlorpian Initiate didnt stand a chance! You see the Phlorpian Initiates guts on the ground.')
                    del rooms[currentRoom]['monster'] # removes the rooms monster
                    rooms[currentRoom]['item'] = 'guts' #drops item in room


  if 'monster' in rooms[currentRoom] and 'dads lucky charm' in inventory:      
        while player['health'] > 0 and aliens['Phlorpian Zealot']['health'] > 0: #fight till somethin dies
            combat_choice = input('Do you want to fight or escape?') # input choice to fight or attempt escape
            if combat_choice == 'fight': # if fight, combat starts
                player_damage= random.randint(0,10) #damage for player 
                #hp reduction for monster based on player attack
                aliens['Phlorpian Zealot']['health'] = aliens['Phlorpian Zealot']['health'] - player_damage
                print('you use your blaster to damage the Phlorpian Zealot for', player_damage, 'the Phlorpian Zealot has', aliens['Phlorpian Zealot']['health'], 'health remaining\n---------------------------' )
                time.sleep(1.5) #gives scroll time
                zealot_attack = random.choice(spell_or_attack)
                if zealot_attack == 'attack':
                    alien_damage = random.randint(0,10) #damage for monster
                    player['health'] = player['health'] - alien_damage # reduction of player health based on monster attack
                    print('The Phlorpian Zealot blasts you with his Schlon Staff for', alien_damage, 'you have', player['health'], 'health remaining.\n ---------------------------')
                else: 
                    lesser_heal = random.randint(0,5) #rolls heal nuber
                    aliens['Phlorpian Zealot']['health'] = aliens['Phlorpian Zealot']['health'] + lesser_heal
                    print('The Phlorpian Zealot HEALED itself for', lesser_heal, 'the Phlorpian Zealot has', aliens['Phlorpian Zealot']['health'], 'health remaining')

##escape option if statements 
            elif combat_choice == 'escape':
                escape_outcome = random.choice(escape_chance) #rolls to see if you can escape

                if escape_outcome == 'successful':
                    currentRoom = random.choice(list(rooms.keys())) #if you escape puts you in a random room on the spaceship
                    print('you escaped successfully to', currentRoom, "! That was a close one.")
                    break 
                elif escape_outcome == 'unsuccessful': #take damage if you roll unsuccessful escape
                    alien_damage = random.randint(0,5)
                    player['health'] = player['health'] - alien_damage
                    print('You failed to escape and the Phlorpian Zealot hit you for', alien_damage, 'you have', player['health'], 'health remaining.')

            else: #what happens if you put anything other than escape or attack
                print('It looks like you only have 2 options in this predicament that you have found yourself in. please choose fight or escape.')

            if aliens['Phlorpian Zealot']['health'] <= 0: #ends combat 
                print('Good job! That Phlorpian Zealot didnt stand a chance! You see where the Phlorpian Zealots body was a scroll of glokin restoration is on the ground.')
                del rooms[currentRoom]['monster'] # removes the rooms monster
                rooms[currentRoom]['item'] = 'scroll of glokin' #drops item in room

  
  if 'monster' in rooms[currentRoom] and 'dads lucky charm' in inventory:
        while player['health'] > 0 and aliens['Phlorpian Berserker']['health'] > 0: #fight till somethin dies
                combat_choice = input('Do you want to fight or escape?') # input choice to fight or attempt escape
                if combat_choice == 'fight': # if fight, combat starts
                    player_damage= random.randint(0,10) #damage for player 
                #hp reduction for monster based on player attack
                    aliens['Phlorpian Berserker']['health'] = aliens['Phlorpian Berserker']['health'] - player_damage
                    print('you use your blaster to damage the Phlorpian Berserker for', player_damage, 'the Phlorpian Berserker has', aliens['Phlorpian Berserker']['health'], 'health remaining\n---------------------------' )
                    time.sleep(1.5) #gives scroll time
                    alien_damage = random.randint(5,55) #damage for monster
                    player['health'] = player['health'] - alien_damage # reduction of player health based on monster attack
                    print('The Phlorpian Berserker goes into a rage slamming you to the ground for', alien_damage, 'you have', player['health'], 'health remaining.\n ---------------------------')

##escape option if statements 
                elif combat_choice == 'escape':
                    escape_outcome = random.choice(escape_chance) #rolls to see if you can escape

                    if escape_outcome == 'successful':
                        currentRoom = random.choice(list(rooms.keys())) #if you escape puts you in a random room on the spaceship
                        print('you escaped successfully to', currentRoom, "! That was a close one.")
                        break
                    elif escape_outcome == 'unsuccessful': #take damage if you roll unsuccessful escape
                        alien_damage = random.randint(0,10)
                        player['health'] = player['health'] - alien_damage
                        print('You failed to escape and the Phlorpian Berserker hit you for', alien_damage, 'you have', player['health'], 'health remaining.')

                else: #what happens if you put anything other than escape or attack
                    print('It looks like you only have 2 options in this predicament that you have found yourself in. please choose fight or escape.')

                if aliens['Phlorpian Berserker']['health'] <= 0: #ends combat 
                    print('Good job! That Phlorpian Berserker didnt stand a chance! You see a health potion on the ground.')
                    del rooms[currentRoom]['monster'] # removes the rooms monster
                    rooms[currentRoom]['item'] = 'health potion' #drops item in room 

  if 'monster' in rooms[currentRoom] and 'dads lucky charm' in inventory:
        while player['health'] > 0 and aliens['Phlorpian Brute']['health'] > 0: #fight till somethin dies
                combat_choice = input('Do you want to fight or escape?') # input choice to fight or attempt escape
                if combat_choice == 'fight': # if fight, combat starts
                    player_damage= random.randint(0,15) #damage for player 
                #hp reduction for monster based on player attack
                    aliens['Phlorpian Brute']['health'] = aliens['Phlorpian Brute']['health'] - player_damage
                    print('you use your blaster to damage the Phlorpian Brute for', player_damage, 'the Phlorpian Brute has', aliens['Phlorpian Brute']['health'], 'health remaining\n---------------------------' )
                    time.sleep(1.5) #gives scroll time
                    alien_damage = random.randint(5,55) #damage for monster
                    player['health'] = player['health'] - alien_damage # reduction of player health based on monster attack
                    print('The Phlorpian Brute slashes you with his Grok for', alien_damage, 'you have', player['health'], 'health remaining.\n ---------------------------')

##escape option if statements 
                elif combat_choice == 'escape':
                    escape_outcome = random.choice(escape_chance) #rolls to see if you can escape

                    if escape_outcome == 'successful':
                        currentRoom = random.choice(list(rooms.keys())) #if you escape puts you in a random room on the spaceship
                        print('you escaped successfully to', currentRoom, "! That was a close one.")
                        break
                    elif escape_outcome == 'unsuccessful': #take damage if you roll unsuccessful escape
                        alien_damage = random.randint(0,10)
                        player['health'] = player['health'] - alien_damage
                        print('You failed to escape and the Phlorpian Brute hit you for', alien_damage, 'you have', player['health'], 'health remaining.')

                else: #what happens if you put anything other than escape or attack
                    print('It looks like you only have 2 options in this predicament that you have found yourself in. please choose fight or escape.')

                if aliens['Phlorpian Brute']['health'] <= 0: #ends combat 
                    print('Good job! That Phlorpian Brute didnt stand a chance! You see the Phlorpian Berserkers Grok on the ground.')
                    del rooms[currentRoom]['monster'] # removes the rooms monster
                    rooms[currentRoom]['item'] = 'Grok' #drops item in room



  if 'monster' in rooms[currentRoom] and 'dads lucky charm' in inventory:
        while player['health'] > 0 and aliens['Fad Cheeser']['health'] > 0: #fight till somethin dies
            combat_choice = input('Do you want to fight or escape?') # input choice to fight or attempt escape
            if combat_choice == 'fight': # if fight, combat starts
                player_damage= random.randint(0,15) #damage for player 
                #hp reduction for monster based on player attack
                aliens['Fad Cheeser']['health'] = aliens['Fad Cheeser']['health'] - player_damage
                print('you use your blaster to damage the Fad Cheeser for', player_damage, 'the Fad Cheeser has', aliens['Fad Cheeser']['health'], 'health remaining\n---------------------------' )
                time.sleep(1.5) #gives scroll time
                Fad_attack = random.choice(spell_or_attack)
                if Fad_attack == 'attack':
                    alien_damage = random.randint(0,25) #damage for monster
                    player['health'] = player['health'] - alien_damage # reduction of player health based on monster attack
                    print('The Fad Cheeser blasts you with his Flogger for', alien_damage, 'you have', player['health'], 'health remaining.\n ---------------------------')
                else:
                    Fad_spell = random.choice(which_spell) #chooses which spell Fad uses
                    if Fad_spell == 'moderate heal':
                        Fad_spell= random.randint(0,10)
                        aliens['Fad Cheeser']['health'] = aliens['Fad Cheeser']['health'] + Fad_spell
                        print('Fad Cheeser healed himself for', Fad_spell, 'Fad now has', aliens['Fad Cheeser']['health'], 'health remaining.') 
                    else:

                        Holy_Fire= random.randint(0,40)
                        player['health'] = player['health'] - Holy_Fire
                        print('Fad looks to the heavens and calls down Holy Fire at your location inflicting', Holy_Fire, 'damage. you now have', player['health'], 'remaining.')
                    

##escape option if statements 
            elif combat_choice == 'escape':
                escape_outcome = random.choice(escape_chance) #rolls to see if you can escape

                if escape_outcome == 'successful':
                    currentRoom = random.choice(list(rooms.keys())) #if you escape puts you in a random room on the spaceship
                    print('you escaped successfully to', currentRoom, "! That was a close one.")
                    break
                elif escape_outcome == 'unsuccessful': #take damage if you roll unsuccessful escape
                    greater_heal = random.randint(0,55)
                    aliens['Fad Cheeser']['health'] = aliens['Fad Cheeser']['health'] + greater_heal
                    print('You failed to escape and Fad Cheeser healed himself for', greater_heal, 'health. Fad now has', aliens['Fad Cheeser']['health'], 'health remaining.')

            else: #what happens if you put anything other than escape or attack
                print('It looks like you only have 2 options in this predicament that you have found yourself in. please choose fight or escape.')

            if aliens['Fad Cheeser']['health'] <= 0: #ends combat 
                print('Youve done it... Idk how but damn you actually did it... you took out the Phlorpian High Priest Fad Cheeser even though he manipulated you into allowing the Phlorpians on board to kill your whole crew... you alone have survived. now take his ring as your prize as it is the new key to the only escape pod.')
                del rooms[currentRoom]['monster'] # removes the rooms monster
                rooms[currentRoom]['item'] = 'Fad Cheesers ring' #drops item in room




##win/lose conditions
  if player['health'] <= 0:
    print('You have been slayne in combat. What a sad end to this story. Try again.')
    break

  if move[0].lower()== 'kill' and move[1].lower()== 'chad':
    print("Covered in the blood of a seemingly kind and helpful man, you feel a sense of relief. You're not sure why but your heart tells you humanity and your ship are better off with him gone.\n----------------------\n Play Again you sly dog you ;)")
    break 

  if currentRoom  == 'Escape Pod' and 'Fad Cheesers ring' in inventory:
    print('you confidently touch Fad Cheesers ring to the consol of the escape pod. As the pod launches off towards the nearest planet, you cant help to think back to your time aboard your ship with your crew. They were all such wonderful people who deserved life with their families back on Earth. None of them fell prey to the Phlorpians tricks and yet they are all dead and you are here. As the ship exits your line of sight,you cant help but think about what life would be if you had just typed "kill Chad" into your terminal.')
    break

