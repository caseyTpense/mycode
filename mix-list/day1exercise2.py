#!/usr/bin/env python3
import random

#wordbank
wordbank= ["four", "spaces"] 

#list of students
tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]

#randomize the list
random.shuffle(tlgstudents)

#slicing name from list based on input
stu= int(input("Pick a student between 0 and 17!\n"))
student_name= tlgstudents[stu]

#displays output
print(student_name, "always uses", wordbank[0], wordbank[1], "to indent")


