import random
attempt = 0
print("Number guessing Game")
computers_guess = random.randint(1,50)
while True:
    users_guess = int(input("Guess the Number: "))
    attempt = attempt +1
    if users_guess == computers_guess:
        print(" You guessed it Right !!! ")
        print("Total Number of Attempts: ",attempt)
        if attempt <=5:
            print(" You earned 100 points")
        else:
            print(" You earned 50 points")
            break
    elif users_guess > computers_guess:
        print("Your Guess is high")
    elif users_guess < computers_guess:
        print("Your Guess is Low")