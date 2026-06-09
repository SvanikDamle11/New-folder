import random
print("Rock Paper Scissors Game")
options = ['Rock', 'Paper', 'Scissors']
while True:
    computers_choice = random.choice(options)
    users_choice = input("Choose Rock Paper Scissors :")
    print("Computers choice:", computers_choice)
    print("Users choice: ",users_choice)

    if users_choice == computers_choice:
        print("Tie!")
    elif users_choice == "Rock":
        if computers_choice == "Scissors":
            print("You win!")
        else: # paper
            print("You lose!")
    elif users_choice == "Paper":
        if computers_choice == "Rock":
            print("You win!")
        else: # scissors
            print("You lose!")
    elif users_choice == "Scissors":
        if computers_choice == "Paper":
            print("You win!")
        else: # rock
            print("You lose!")