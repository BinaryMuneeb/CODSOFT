while True:
    print("WELCOME TO SIMPLE AIRTHMATIC CALULATOR")
    print("-----------------------------------------")
    # option which airthmatic function do you perform from this calculation
    print("enter operator from +,-,*,/ ( from user choice) :")
    # user give his input which function his perform
    user_input=input("enter what function do you perform :")
    # first input of user input
    number1=float(input("enter the first number :"))
    # 2nd input of user input
    number2=float(input("enter second number :"))
    # match keyword match operator which function does user wont to perform
    match user_input:
        case "+":
            print("the sum of given to number is ",number1+number2)

        case "-":
            print("the subtraction of given to number is ", number1 - number2)
        case "*":
            print("the product of given to number is ", number1 * number2)
        case "/":
            print("the dividion of given to number is ", number1 / number2)
        # if function is not in give option they ru defualt case
        case _:
            print("select user input from givin option ")
    # if user wont to perform another calulation or not write yes or no
    again_calcultion=input("if you wont to perform another calculation (y/n) :")

    if again_calcultion =='NO':

        break
print("thanks for using calculator")