import random

computed_number = random.randint(1, 100)

player_lives = None

print('Welcome to the number guessing game!')

difficulty = input('On what difficulty do you want to play? [E]asy or [D]ifficult: \n').lower()
if difficulty == 'e':
    player_lives = 10
    print(f'You selected easy, so you have {player_lives} lives!')
elif difficulty == 'd':
    player_lives = 5
    print(f'You selected difficult, so you have {player_lives} lives!')


while player_lives > 0:
    player_guess = int(input('What number am I thinking? \n'))

    if player_guess == computed_number:
        print('You guessed correctly!')
        player_lives = 0

    elif player_guess > computed_number:
        print('Too high!')
        player_lives -= 1
        print(f'Lives left: {player_lives}')

    elif player_guess < computed_number:
        print('Too low')
        player_lives -= 1
        print(f'Lives left: {player_lives}')

print(f'Game over!')
