import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == "Q":
        break
    
    if user_input == "rock" and computer_guess == "paper":
        print("you win!")
    if user_input not in ["rock", "paper", "scissors"]:
        print("Type in value")