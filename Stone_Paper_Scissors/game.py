
import random
user_point=0
computer_point=0
while True:
        options = ['stone','paper','scissor']
        user_input = input("stone/paperr/scissor or q for quit : ").lower()
        if user_input=='q':
            break
        elif user_input not in options:
            print("Not in option")
            continue
        random_number = random.randint(0,2)
        computer_picker = options[random_number]
        print("Computer picked",computer_picker,'.')
        if user_input=="paper" and computer_picker=="stone":
            print("User won!")
            user_point+=1
        elif user_input=="scissor" and computer_picker=="paper":
            print("User won!")
            user_point+=1
        elif user_input=="stone" and computer_picker=="scissor":
            print("User won!")
            user_point+=1
        else:
            print("Computer won!")
            computer_point+=1
print("User point is : ",user_point)
print("Computer point is : ",computer_point)
print("Goodbye")
