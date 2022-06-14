def ChineseZodiac(year:int):
    Zod_dict = {0:"Dragon", 1:"Sanke", 2:"Horse", 3:"Sheep", 4:"Monkey", 5:"Rooster", 6:"Dog", 7:"Pig", 8:"Rat", 9:"Ox", 10:"Tiger", 11:"Hare"}
    chin_year = (year-2000) % 12
    sign = Zod_dict[chin_year]
    return sign

    birth_year = int(input("Input your birth year: "))
        print("Your Zodiac sign is :",ChineseZodiac(birth_year))

