#!/usr/bin/env python3

farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]} ,
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

animal = ["chickens", "sheep", "cows", "pigs", "llamas", "cats"]
plants = ["carrots", "celery", "bananas", "apples", "oranges",]


for x in farms:
    print("-", x["name"])
farm_choice= input("choose a farm!\n")
for x in farms:
    if x["name"].lower() == farm_choice.lower():
        print("-", x["agriculture"])
        for animals in x["agriculture"]:
            if animals in animal:
                print(animals)
