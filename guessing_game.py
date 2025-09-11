import random

def guess(x):
    number = random.randint(1,x)
    guess = 0
    while number != guess:
        guess = int(input("Guess a number : "))
        if guess > number:
            print(f"{guess} is too high!")
        elif guess < number:
            print(f"{guess} is too low!")
        
    print(f"Yay! You've guessed the correct number. The number is {guess}")

def computer_guess(x):
    low = 1
    high = x
    feedback= ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else :
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C): ")
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
        
    print(f"Yay! The computer has guessed your number, {guess}, correctly!")

guess(10)