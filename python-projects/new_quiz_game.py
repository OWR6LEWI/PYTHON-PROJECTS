print("welcome to my quiz game!! ")

playing = input("Do you wish to play? ")

while playing.lower() != "yes":
    print("Please type yes to continue")
    playing = input("Do you wish to play?")
else:
    print("Okay let's play!! ")
    score = 0

question = input("What is the capital of France? ")

while question.lower() != "paris":
    print("Incorrect! Try again.")
    question = input("What is the capital of France?")

else:
    print("Correct!")
    score += 1

question = input("What is the capital of south africa? ")

while question.lower() != "cape town":
    print("Incorrect! Try again.")
    question = input("What is the capital of south africa? ")
else:
    print("Correct!")
    score += 1

question = input("What is the capital of china? ")

while question.lower() != "beijing":
    print("Incorrect! Try again.")
    question = input("What is the capital of china? ")
else:
    print("Correct!")
    score += 1

# print("You got " + str(score) + " questions correct!")
print(f"You got {score} questions correct!")
print("You got " + str((score/3) * 100) + "%. ")
print(str(score) + "/3 questions answered correctly ")

print("Well done!!")
