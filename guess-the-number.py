from random import randint
from time import sleep
from os import system, name

logo = '''
   ___                     _____ _              __                 _               
  / _ \_   _  ___  ___ ___/__   \ |__   ___  /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| / /\/ '_ \ / _ \/  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \/ /  | | | |  __/ /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/\/   |_| |_|\___\_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
'''
def clear(): # clear the screen
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def play():

    clear()
    print(logo)
    sleep(2)
    print('I have a number between 1 and 100. Can you guess it in time?')
    print('Do you want to play easy (10 guesses) or hard (5 guesses)? ')
    guesses_left = int(input('> '))
    choice = randint(1,100)
    print(choice)
    guessed_correct = False
    while guesses_left > 0 and not guessed_correct:
        guess = int(input(f'{guesses_left} guesses left. Guess? '))
        guesses_left -= 1
        if guess > choice:
            print('Too high!')
        elif guess < choice:
            print('Too low!')
        else:
            guessed_correct = True
    else:
        if guessed_correct:
            print(f'Congrats you have won with {guesses_left} guesses left. My number was {choice}')
        else:
            print(f'Unlucky you lose, you have run out of guesses! My number was {choice}')
    play() if input('Play again Y/n').lower() == 'y' else quit()

play()
