print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
crossroad = input("You are a crossroad where do you want to go? type 'left' or 'right'").lower()
if crossroad == "left":
    print("You've come to lake. There is an island in the middle of the lake.")
    boat = input("Type 'wait' to wait for a boat. type 'swim' to swim across.").lower()
    if boat == "wait":
        print("there are 3 doors to choose")
        door = input("Type R for red, B for blue and Y for yellow door")
        if door == "R":
            print("You are burned by fire. Game Over")
        elif door == "B":
            print("Eaten by beasts. Game Over")
        elif door == "Y":
            print("You Win!!!!")
        else:
            print("Game Over, you choose wrong option.")            
    else:
        print("Attacked by trout. Game Over")    
else:
    print("You've fell into a hole. Game Over!")    