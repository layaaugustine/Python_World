
print("Welcome To Quiz World!!!")

def game():
    score=0
    Question = input("Which keyword allows us to load a module in Python? ")

    if Question.lower() == "import":
        print("Correct !..")
        score+=1
    else:
        print("Incorrect !..")
        print(score)

    Question = input("Which one from the following objects in Python is immutable? ")

    if Question.lower() == "tuple":
        print("Correct !..")
        score+=1
    else:
        print("Incorrect !..")
        print(score)

    Question = input("The ________ module is used for creating and manipulating DataFrames in Python? ")

    if Question.lower() == "pandas":
        print("Correct !..")
        score+=1
    else:
        print("Incorrect !..")
        print(score)

    Question = input("Which one of the following operators can perform floor division in Python? ")

    if Question.lower() == "//-":
        print("Correct !..")
        score+=1
    else:
        print("Incorrect !..")
        print(score)

    Question = input("Which function can add elements to the end of a list? ")

    if Question.lower() == "append()":
        print("Correct !..")
        score+=1
    else:
        print("Incorrect !..")
        print(score)

    print(f'You got {score} out of 5')
while True:

    playing = input("Do you want to play? ")
    if playing.lower()!="yes":
        quit()
    else:
        print("Okay! Let's play")
        game()
