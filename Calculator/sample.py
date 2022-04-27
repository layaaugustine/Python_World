print("!!! CALCULATOR !!!")

'''
1, Add
2, Substraction
3, Multiplication
4, division

'''

def calculator():
    if operator == '+':
        print("Sum of two number : ",number_1+number_2 )
    elif operator=='-':
        print("Substraction of two number : ",number_1-number_2 )
    elif operator=='*':
        print("Multiplication of two number : ",number_1*number_2 )
    elif operator == '/':
        print("Division of two number is : ",number_1/number_2)
    else:
        print("Invalid Operator !")
        exit()

while True:
    print("Enter Two Numbers")
    number_1 = input("Enter First Number : ")
    operator = input("Enter an operator : ")
    number_2 = input("Enter Secound Number : ")
    if number_1.isdigit() and number_2.isdigit():
        number_1=int(number_1)
        number_2=int(number_2)
    else:
        print("Enter a number !!")
        break
    calculator()
print("gudbye")