# This got succesful :)

import random

choices = ['rock', 'paper', 'scissors']
times = int(input('How many times do you need to do Rock paper and Scissors? '))
i = 1
wins_user = 0
wins_system = 0

while i <= times:

    user = input('Enter your option: ').lower()
    system = random.choice(choices)

    if user == system:
        print(f'It is a tie -  your choice: {user} and system choice: {system}')
        i = i + 1
    elif (user == 'rock' and system == 'scissors') or (user == 'paper' and system == 'rock') or (user == 'scissors' and system == 'paper'):
        print(f'You got that one - your choice: {user} and system choice: {system}')
        wins_user += 1
        i = i + 1
    elif (user == 'rock' and system == 'paper') or (user == 'paper' and system == 'scissors') or (user == 'scissors' and system == 'rock'):
        print(f'Oh! man it is for the system - your choice: {user} and system choice: {system}')
        wins_system += 1
        i = i + 1
    else:
        print('You your shit input is invalid')
        break

else:
    print('\n')
    if wins_system == wins_user:
        print(f'IT IS A TIE! Your wins: {wins_user} and System wins: {wins_system}')
    elif wins_user > wins_system:
        print(f'YOU WIN! Your wins: {wins_user} and System wins: {wins_system}')
    elif wins_user < wins_system:
        print(f'Damn, the system wins, System wins: {wins_user} and System wins: {wins_system}')