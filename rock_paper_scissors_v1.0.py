#This will be a code to play rock paper scissors against a cpu!
import random  

print("Welcome to my rock paper scissors game! v1.0")

#list for computer to choose
list = ["rock", "paper", "scissors"]
computer_choice = random.choice(list)

#for player
player_choice = input("Choose your move!: ")

#programme starts
if player_choice == computer_choice:
    print("You chose " + player_choice + " and it's a tie!")
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("Computer chose " + computer_choice + ". You win!")
    else:
        print("Computer chose " + computer_choice + ". You lose!")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("Computer chose " + computer_choice + ". You win!")
    else:
        print("Computer chose " + computer_choice + ". You lose!")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("Computer chose " + computer_choice + ". You win!")
    else:
        print("Computer chose " + computer_choice + ". You lose!")
