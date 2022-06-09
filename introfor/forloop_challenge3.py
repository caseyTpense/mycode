#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
animal = ["chickens", "sheep", "cows", "pigs", "llamas", "cats"]
plants = ["carrots", "celery", "bananas", "apples", "oranges",]
NE_animals= farms[0]["agriculture"]
for x in farms:
    print("-", x["name"])
farm_choice= input("choose a farm!\n")
for x in farms:
    if x["name"].lower() == farm_choice.lower():
        print("-", x["agriculture"])
        for animals in x["agriculture"]:
            if animals in animal:
                print(animals)

