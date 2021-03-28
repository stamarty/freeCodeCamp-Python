## Computer will guess your number!! 

import random

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    count = 0

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
            count = count + 1
        else:
            guess = low
            count = count + 1
        
        feedback = input(f'Compy guessed {guess}, is that too (H)igh, (L)ow or (C)orrect? ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Compy guessed {guess} correctly, it took {count} tries!')

comp_guess(10000)
