print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
# attempts = 3
# import pdb:
answer = input("What does CPU stand for? ")
# pdb.set_trace()
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('incorrect!')
    # continue((answer = input("what does CPU stand for? "))

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('incorrect!')
    # continue(answer = input("what does GPU stand for? "))

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('incorrect!')
    # continue((answer = input("what does RAM stand for? "))

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print('incorrect!')
    # continue((answer = input("what does PSU stand for? "))

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%. ")
print(str(score) + "/4 questions answered correctly")
