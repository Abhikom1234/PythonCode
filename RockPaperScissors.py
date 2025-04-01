#This is a rock, paper and scissors game!
import random
def value():
    options = ["rock", "paper", "scissors"]
    while True:
        player_choice = input("Enter rock, paper or scissors: ").lower()
        if player_choice in options:
            break
        else:
            print("Invalid input! Please choose rock, paper or scissors.")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check(player, computer):
    print("Player chose: ", player , " Computer chose: ", computer)
    if player == computer:
        print("Its a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You Win!")
        else:
            print("You Lose!")
    elif player == "paper":
        if computer == "rock":
            print("You Win!")
        else:
            print("You Lose!")
    elif player == "scissors":
        if computer == "paper":
            print("You Win!")
        else:
            print("You Lose!")
choices = value()
check(choices["player"], choices["computer"])
