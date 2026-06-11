import random


secret = random.randint(1, 50)

max_attempts = 5
attempts = 0
won = False

print("🎯 Welcome to the Number Guessing Game! 🎯")
print("I'm thinking of a number between 1 and 50. You have 5 attempts to guess it.")
print("-" * 50)

while attempts < max_attempts:
    
    guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
    attempts += 1

    if guess == secret:
        won = True
        break
    
    difference = abs(guess - secret)
    if difference <= 2:
        hint = "🔥 hot"
    elif difference <= 5:
        hint = "🌡️ warm"
    elif difference <= 10:
        hint = "🥶 cold"
    else:
        hint = "🧊 ice cold"
        
    print(f"Hint: Your guess is {hint}!")

    remaining_lives = max_attempts - attempts
    print("Remaining lives: ", end="")
    for i in range(remaining_lives):
        print("❤️", end="")
    print()  # Moves to the next line

print("-" * 50)

if won:
    print(f"🎉 Congratulations! You guessed the secret number {secret} in {attempts} attempts! 🎉")
else:
    print(f"💥 Game Over! The secret number was {secret}. Better luck next time! 💥")