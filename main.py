import random

computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (r for rock, p for paper, s for scissor): ").lower()

youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "rock", -1: "paper", 0: "scissor"}

if youstr not in youDict:
    print("Invalid input! Please choose 'r' for rock, 'p' for paper, or 's' for scissor.")
else:
    you = youDict[youstr]
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a Draw")
    else:
        if (you == 1 and computer == 0):
            print("You win!")
        elif (you == 0 and computer == 1):
            print("You lose!")
        elif (you == -1 and computer == 1):
            print("You win!")
        elif (you == 1 and computer == -1):
            print("You lose!")
        elif (you == 0 and computer == -1):
            print("You win!")
        elif (you == -1 and computer == 0):
            print("You lose!")
        else:
            print("Something went wrong")
