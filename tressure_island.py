print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision_on_direction=input("Do you want to go left or right? ").lower()
if decision_on_direction=="left":
    decision_on_action=input("Do you want to Swim or Wait for the Boat to arrive? ").lower()
    if decision_on_action=="wait":
        print("Your Boat has arrived. You can move to island unharmed")
        decision_on_doors= input("Now there are 3 doors ahead in the island i.e Red, Blue and Yellow. Which one will you choose?").lower()
        if decision_on_doors=="red":
            print("Oh no! that Red room was full of fire. \nGAME OVER.\n Better Luck Next time!")
        elif decision_on_doors=="blue":
            print("Oh no! that Blue room was full of Poisonus gas. \nGAME OVER.\n Better Luck Next time!")
        elif decision_on_doors=="yellow":
            print("Congratulations! You Won! your chosen room turned out to be full of tressure!. \nGAME OVER.")
        else:
            print("I think Something is wrong with your input. \n GAME OVER.")
    else:
        print("Oh! no. If you Swim then crocodiles will have you for their Dinner/Launch.\nGAME OVER\n Better luck next time!")

else:
    print("Oh! no, moving into that direction made you to fall in a big pit. \nGAME OVER.\n Better Luck Next time!")