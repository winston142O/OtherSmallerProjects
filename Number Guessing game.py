import random
secret = random.randrange(1, 16)
guess = 0
tries = 0


while guess != secret:
    guess = int(input("Try to guess the number between 1 and 15."))
    tries = tries + 1
    if guess > secret:
        print("Nope, too high.")
    elif guess < secret:
        print("Nope, too low.")
    else:
        print("That is correct.")
        
print("Number of tries:", tries)
