import random
problems = int(input("How many math problems would you like to practice? "))
counter = 0
numberCorrect = 0
while counter < problems:
    randNumber1 = random.randrange(1,50)
    randNumber2 = random.randrange(1,50)
    correctAnswer = int(randNumber1 + randNumber2)
    yourAnswer = int(input(f"What is the integer value of {randNumber1} + {randNumber2}?"))
    if correctAnswer == yourAnswer:
        print("Good job! You answered correctly.")
        numberCorrect += 1
    else:
        print(f"You got the answer incorrect, it was {correctAnswer}.")
    counter += 1

print(f"You answered {numberCorrect} of the {problems} problems correctly.")
print("Thank you for playing")