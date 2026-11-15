print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|
          |                `"=._o`"=._      _`"=._
 _________|_____________________:=._o "=._."_.-="'"=.
|                   |    __.--" , ; `"=._o." ,-"""-.
|___________________|_.-"  /  / \  \  `"=._"|
          |          |  /  /   \  \   |  |
*******************************************************************************
''')
choice1=input("you are at a cross road tellme you want to go left or right :-").lower()

if choice1=='left':
    choice2=input("you want to wait for boat or swim").lower()
    if choice2=='wait':
        choice3=input("select door from the available door red or yellow or blue").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over!")

        elif choice3 == "yellow":
            print("You found the treasure! You Win!")

        elif choice3 == "blue":
            print("You entered a room full of beasts. Game Over!")

        else:
            print("You chose a door that doesn't exist. Game Over!")


    else:
       print("you are eaten by grook")
else:
    print("you fall into hole.")