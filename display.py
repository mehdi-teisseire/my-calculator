# Inputs
def input_operation():
    return input("Please type your operation:\n")

# Messages
def message_welcome():
    print("Welcome to MyCalculator®!")

def message_file_create():
    pass

def message_file_exist():
    pass

# Errors
def error_format():
    print("Invalid format!")

def error_invalid_chara():
    print("Invalid characted detected!")

def error_division_zero():
    print("Can't divide by 0! (would make +∞, -∞ or 0 anyway)")

def error_not_openable():
    print("Something went wrong when opening the file!")

def error_not_writable():
    print("Something went wrong when writing the file!")

def error_not_saving():
    pass

def error_append_file():
    pass

def error_not_deleted():
    pass

def error_file_not_exist():
    pass
 
def error_reset_failed():
    pass

# History
def history(value): #TODO temp variable; Need to know what History returns
    print(value)

# Result
def result(value): #TODO temp variable; Need to know how to print result
    print(f"= {value}")