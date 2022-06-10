import random
player = {'health' : int(50), 'attack' : random.randint (0,5),}

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
                }
            }


  
def combat():
#    while player['health'] > 0 and aliens['Phlorpian Grunt']['health'] > 0:
        for enemy in aliens:
            print("the ". enemy, "is ready to battle!")
           # combat_choice = input('Do you want to strike or attempt to flee?')
       #if combat choice == 'strike':


combat() 
