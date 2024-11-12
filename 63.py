# Snake, Water and Gun is a variation of the children's game 
# "rock-paper-scissors" where players use hand gestures to represent a snake, 
# water, or a gun. The gun beats the snake, the water beats the gun, and the 
# snake beats the water. Write a python program to create a Snake Water Gun game in Python using
# if-else statements. Do not create any fancy GUI. Use proper functions to check for win.
import random
a="hi! this is rock paper ciser game"
x="enter your move (r,p,c):"
k=["R","P","C"]
v = random.choice(k)
print(v)
print(a.title())
b=input(x.title()).upper()

if b in k:
    
    if(b =="R"or b == "P" or b == "C"):
        if(b=="R" and v=="R"):
            print("draw npc choose S and you too ")
        elif(b=="P" and v=="P"):
            print("draw npc choose p and you too ")
        elif(b=="C"and v=="C"):
            print("draw npc choose C and you too ")
        else:
            if(b=="R" and v=="P"):
             print(" npc win choose p and you lose ")
            elif(b=="C" and v=="P"):
             print(" npc lose He choose p and you win :) ")
            else:
                if(b=="C" and v=="R"):
                 print(" npc win He chooe S and you lose ")
                elif(b=="P" and v=="R"):
                 print(" npc lose He choose S and you win :) ")
                else:
                    if(b=="P" and v=="C"):
                     print(" npc win He choose C and you lose ")
                    elif(b=="R" and v=="C"):
                     print(" npc lose He choose C and you win :) ")
else:
    print("enter your three worlds ")

                    
            