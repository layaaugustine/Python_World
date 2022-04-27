
import random
number = input("Type a number : ")

if number.isdigit():
    number = int(number)
    if number <=0:
        print("Please type a number greater than 0...")
        quit()
else:
    print("Please type a number...")
    quit()
random_number = random.randint(0,number)

print("random_number is",random_number)

guess=0
while True:
    guess+=1
    user_guess = input("Guess the number : ")

    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number...")
        continue
    if user_guess==random_number:
        print("you got it!...")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("you got it in",guess)