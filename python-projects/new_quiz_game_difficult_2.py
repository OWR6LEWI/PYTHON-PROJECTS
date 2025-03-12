print("Welcome to my quiz game!!")

playing = input("Do you wish to play? ")

while playing.lower() != "yes":
    print("Please type yes to continue")
    playing = input("Do you wish to play?")

print("Okay, let's play!!")
score = 0  # Initialize score

# Choose difficulty level
difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
if difficulty == "easy":
    max_attempts = 5
elif difficulty == "medium":
    max_attempts = 3
else:
    max_attempts = 1

# Question 1
attempts = max_attempts  # Set attempts based on difficulty
question = input("What is the capital of France? ")

while question.lower() != "paris" and attempts > 1:
    attempts -= 1
    print(f"Incorrect! Try again. You have {attempts} attempts left.")
    question = input("What is the capital of France? ")

if question.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Out of attempts! The correct answer is Paris.")

# Question 2
attempts = max_attempts  # Reset attempts
question = input("What is the capital of South Africa? ")

while question.lower() != "cape town" and attempts > 1:
    attempts -= 1
    print(f"Incorrect! Try again. You have {attempts} attempts left.")
    question = input("What is the capital of South Africa? ")

if question.lower() == "cape town":
    print("Correct!")
    score += 1
else:
    print("Out of attempts! The correct answer is Cape Town.")

# Question 3
attempts = max_attempts  # Reset attempts
question = input("What is the capital of China? ")

while question.lower() != "beijing" and attempts > 1:
    attempts -= 1
    print(f"Incorrect! Try again. You have {attempts} attempts left.")
    question = input("What is the capital of China? ")

if question.lower() == "beijing":
    print("Correct!")
    score += 1
else:
    print("Out of attempts! The correct answer is Beijing.")

# Display final score
print(f"You got {score} questions correct!")
print(f"You got {(score / 3) * 100:.2f}%.")
print(f"{score}/3 questions answered correctly.")
print("Well done!")
