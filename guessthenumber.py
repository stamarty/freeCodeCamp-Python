import random

def guess(x):
    random_integer = random.randint(1, x)
    guess = 0
    guesscount = 0
    while guess != random_integer:
        guess = int(input(f'Guess a number between 1 and {x}. '))
        print(f'You guessed: {guess}.')
        if guess < random_integer:
            print(f'Your guess of {guess} is too low! ')
            guesscount = guesscount + 1
        elif guess > random_integer:
            print(f'Your guess of {guess} is too high! ')
            guesscount = guesscount + 1
        
    guesscount = guesscount + 1
    print(f'Congratulations! {guess} is the correct number! It took you {guesscount} tries.')
        
guess(100)