#!/usr/bin/env python3

#wordbank
wordbank= ["four", "spaces"] 

#list of students
tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]

while True:
#slicing name from list based on input
    stu= int(input("Pick a student between 0 and 17!\n"))
    student_name= tlgstudents[stu]

    found_stu = False
    for i in tlgstudents:
        found_stu = True
    if found_stu:
        print(stu, "always uses", wordbank[0], wordbank[1], "to indent")

    else:
        print("Please choose another number or a name of a student you know is in the TLG cohort."
