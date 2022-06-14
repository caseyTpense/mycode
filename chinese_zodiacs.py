#!/usr/bin/env python3
def zodiac(year:int): #defining function
  #dictionary for return values  
  zod = {0:"Dragon: you are talented, powerful, lucky, and successfull.", 1:"Snake: you are wise, like to work alone, and determined.", 2:"Horse: you are animated, active, and energetic.", 3:"Sheep: you are creative, resilient, gentle, mild-mannered, and shy.", 4:"Monkey: you are sharp, smart, curious, and mischievious.", 5:"Rooster: you are hardworking, resourceful, courageous, and talented.", 6:"Dog: you are loyal, honest, cautious, and kind.", 7:"Pig: you are a symbol of wealth, honesty, and practicality.", 8:"Rat: you are artistic, sociable, industrious, charming, and intelligent.", 9:"Ox: you are strong, thorough, determined, loyal, and reliable.", 10:"Tiger: you are courageous, enthusiastic, confident, charismatic, and a leader.", 11:" Rabbit: you are vigilant, witty, quick-minded, and ingenious."}
  chinese_year = (year-2000) % 12  #formula to reference zod 
  sign = zod[chinese_year]  #assigning the value of chinese_year in zod to sign
  return sign  #return  the value
birth_year = int(input("Input your birth year: ")) #requests input from user
print("Your Zodiac sign is", zodiac(birth_year)) # displays your results
