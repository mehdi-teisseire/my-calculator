def user_input():    

    try:
        number_1 = float(input("Your first number"))
        number_2 = float(input("Your second number"))
    except ValueError:
        print("Invalid format")

user_input()