# Rock,Paper, Sizer game.
'''
-1 for Rock
0 for Paper
1 for Sizer

'''

import random # import random for computer chose randome number as given

computer = random.choice([-1 , 0 , 1]) 
print("Chose any one of these: (r , p ,s)")
youstr = input("Enter your choice: ")
youdict = {"r": -1 , "p" : 0 , "s" : 1}
reversdict = { -1:"Rock" , 0:"Paper" , 1:"Sizer"}
you = youdict[youstr]

print(f"You chose {reversdict[you]}\n Computer chose {reversdict[computer]}")

if(computer == you):
    print("Game Draw")
else:
    if(computer == -1 and you == 0): 
        print("You Lose!")
    elif(computer == -1 and you == 1):
        print("You Lose!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Win!")
    elif(computer == 1 and you == -1):
        print("You Win!")
    elif(computer == 1 and you == 0):
        print("You Lose!")
    else:
        print("Something went wrong!")