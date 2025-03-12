import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("type Rock/Paper/Scissors: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
         break
    
random_number = random.randint(0, 2)
# rock: 0, paper: 1, scissors: 2
computer_guess = options[random_number]
print("computer guessed", computer_guess + ".")

if user_input == "rock" and computer_guess == "scissors":
     print("You are the winner")
     user_wins += 1

if user_input == "paper" and computer_guess == "rock":
     print("You are the winner")
     user_wins += 1

if user_input == "scissors" and computer_guess == "paper":
     print("You are the winner")
     user_wins += 1

else:
     print("You lost")
     computer_wins += 1

print("goodbye!")