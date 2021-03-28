#import the methods from each of the madlibs
from madlibs import christmas, code, hp, hungergames, zombie
import random

if __name__ == "__main__":
#fill the array with the name of each of the files
    m = random.choice([christmas, code, hp, hungergames, zombie])
    m.madlib()