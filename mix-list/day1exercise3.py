#!/usr/bin/env python3

#wordbank
wordbank= ["four", "spaces"] 

#list of students
tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]

#slicing name from list based on input
stu= (input("Pick a student between 0 and 17!\n"))
#if input is a name in the list it will use that name
if stu in tlgstudents:
    print(stu, "always uses", wordbank[0], wordbank[1], "to indent")
#allows the use of element numbers to be used 
else:
    stu= tlgstudents[int(stu)]
    print(stu, "always uses", wordbank[0], wordbank[1], "to indent")
