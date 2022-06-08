#!/usr/bin/env python3

## collects input from user
hostname = input("What value should we set for hostname?")

## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("Hostname matches expected config")
## always print out 
print("Exiting the script.")

