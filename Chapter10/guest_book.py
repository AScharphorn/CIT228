import random
import os
filename="Chapter10/guest_list.txt"

if os.path.exists(filename):
    os.remove(filename)

"""with open(filename,"a") as guestfile:
    guest=input("Please enter your name (q to quit) ")
    while guest != 'q':
        guestfile.write(guest)
        guest+="\n"
        guest=input("Please enter your name (q to quit) ")"""
    
guest_list=[]
with open(filename,"w") as guestfile:
    guest=input("Please enter your name (q to quit) ")
    while guest != 'q':
        number=random.randint(1,50)
        while number in guest_list:
            number=random.randint(1,50)
        print(f"{guest} you will be in room {number}")
        guest_list.append(number)
        guest+=", room# " + str(number) + "\n"
        guestfile.write(guest)
        guest=input("Please enter your name (q to quit) ")
    
with open(filename) as guestfile:
    print("------ Guest(s) & Room(s) Assigned ------")
    for line in guestfile:
        print(line)