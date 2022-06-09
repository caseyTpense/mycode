#!/usr/bin/env python3


with open("dracula.txt","r") as dracula:
    count=0
    for book in dracula:
       if "vampire" in book.lower():
            count +=1
            print(book)
            print(count)

with open("dracula.txt", "r") as dracula:
    for book in dracula:
        book = book.rstrip('\n')

        if "vampire" in book.lower():
            with open("vampytimes.txt", "a") as srvfile:
                srvfile.write(book +"\n")




