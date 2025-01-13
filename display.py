# Inputs
def input_operation():
    return input("Please type your operation:\n")

# Messages
def message_welcome():
    print("Welcome to MyCalculator®!")

# Errors
def error_format():
    print("Invalid format!")

def error_invalid_chara():
    print("Invalid characted detected!")

def error_division_zero():
    print("Can't divide by 0! (would make +∞, -∞ or 0 anyway)")

# History
def history(value): #TODO temp variable; Need to know what History returns
    print(value)

# Result
def result(value): #TODO temp variable; Need to know how to print result
    print(f"= {value}")