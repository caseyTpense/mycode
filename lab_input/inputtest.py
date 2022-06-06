#!/usr/bin/env python3
# input of a name
# input of a date
# print it all on one line



def main():

    user_input = input("Hi! please tell me your name.:")

    print("Nice to meet you ", user_input)

    day = input ("Could you tell me what day of the week it is?:")
    print("Hello, ", user_input + "! ", " Happy ", day, sep="")



main()


