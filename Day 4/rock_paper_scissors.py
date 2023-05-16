import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# Make the selections
user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
computer_choice = random.randint(0, 2)

# Print the users selection
if user_input == 0:
    print(f'You selected rock \n{rock}')
elif user_input == 1:
    print(f'You selected paper \n{paper}')
elif user_input == 2:
    print(f'You selected scissors \n{scissors}')

# Print the computers selection
if computer_choice == 0:
    print(f'The computer selected rock \n{rock}')
elif computer_choice == 1:
    print(f'The computer selected paper \n{paper}')
elif computer_choice == 2:
    print(f'The computer selected scissors \n{scissors}')

# Draw scenario
if user_input == computer_choice:
    print('It is a draw!')

# Rock - Paper scenario
elif user_input == 0 and computer_choice == 1:
    print('The computer won!')

# Rock - Scissors scenario
elif user_input == 0 and computer_choice == 2:
    print('You won!')

# Paper - Rock scenario
elif user_input == 1 and computer_choice == 0:
    print('You won!')

# Paper - Scissors scenario
elif user_input == 1 and computer_choice == 2:
    print('The computer won!')

# Scissor - Rock scenario
elif user_input == 2 and computer_choice == 0:
    print('The computer won!')

# Scissor - Paper scenario
elif user_input == 2 and computer_choice == 1:
    print('You won!')

# Error catch
else:
    print('You typed an incorrect number. You lose!')