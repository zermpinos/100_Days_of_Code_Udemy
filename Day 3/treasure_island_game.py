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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


# Write your code below this line 👇
first_choice = input('You are at a crossroad . Where do you want to go? Type "left" or "right".').lower().strip()

if first_choice == 'left':
    second_choice = input(
        'You have reached a lake. There is an island in the middle. '
        'Type "wait" to wait for the boat or "swim" to swim across.').lower().strip()
    if second_choice == 'wait':
        third_choice = input(
            'You have reached the island unharmed. '
            'There is a house with 3 doors, one is blue, one is red and one is yellow. '
            'Which do you choose?').lower().strip()
        if third_choice == 'red':
            print('You got burned by a fire. Game Over!')
        elif third_choice == 'blue':
            print('You got eaten by wild beasts. Game Over!')
        elif third_choice == 'yellow':
            print('You win! Congratulations!')
        else:
            print('Game Over!')
    else:
        print('You were attacked by a shark. Game Over!')
else:
    print('You fell into a hole. Game Over!')
