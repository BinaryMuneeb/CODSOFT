while True:

    print("welcome to password generator")

    #for generating strong password generator we use random module
    import random
    #captital letter
    upper_case="ABCDEFGHKLMNOBQRSTWXYZ"
    #small letter
    lower_case="ABCDEFGHIGKLMNOPQRSTWXYZ"
    #NUMBER 0-9
    number="0123456789"
    #special character
    symbols="!@#$%^&?/|}]"
    use_for=upper_case+lower_case+number+symbols
    lenght_of_password =int(input("enter the length of pass-word :"))
    if lenght_of_password>=8:
        password="".join(random.sample(use_for,lenght_of_password))
        print("your generated password is :",password)
    else:
        print("password should be greater >= 8 digits ")
    generated_again=input("would you like to generated password again (yes/no):")
    if generated_again=="no":
        break
print("thanks for using password generator")


