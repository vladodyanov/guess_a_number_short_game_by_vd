import random

computer_number = random.randint(1, 21)
player_name = input('Please enter your name: ')

while True:
    player_input = input('Guess the number between 1 and 21: ')

    if not player_input.isdigit():
        print(f'Invalid input. Try again,{player_name}!')
        continue

    player_number = int(player_input)
    if player_number == computer_number:
        print(f'It is your lucky day, {player_name}. You guess the number !')
        break
    elif player_number > computer_number:
        print('The number you selected is too high! Try again!')
    elif player_number < computer_number:
        print('The number you selected is too low! Try again!')