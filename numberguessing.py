import random
import math
num = round(random.random() * 10)
guesses = 1
right = False

print("Im thinking of a number between 0 and 10. \n                -u-")
print("You get 3 guesses.")
while guesses <= 3:
    uguess = int(input(f"\nGuess {guesses}: "))
    if uguess == num:
        guesses = 4
        print("Correct! You're great at this!")
        break
    elif uguess < num:
        print("Sorry too low, try again!")
        guesses += 1
    elif uguess > num:
        print("Ooh, too high, try again!")
        guesses += 1
else:
    print(f"Aw shucks, the number was {num}\nBetter luck next time!")

print("_" * 30)
print("Goodbye!")
    
        
