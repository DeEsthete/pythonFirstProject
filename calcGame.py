import random

name = input("What is you name?")
print("Hello " + name)


while True:
    operation = random.randint(0, 2)
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    quest = "Quest: "
    correctAnswer = -1
    if (operation == 0):
        quest += str(a) + "+" + str(b)
        correctAnswer = a + b
    elif (operation == 1):
        quest += str(a) + "-" + str(b)
        correctAnswer = a - b
    elif (operation == 2):
        quest += str(a) + "*" + str(b)
        correctAnswer = a * b

    print(quest)
    userAnswer = input("Answer: ")
    if (str(userAnswer) == str(correctAnswer)):
        print("Good, is correct")
    else:
        print("You stupid maaaan")