# Inputs
def input_operation():
    return input("Please type your operation:\n")

# Messages
def message_welcome():
    print("Welcome to MyCalculator®!")

def message_file_open(filename):
    print(f"Data successfully saved to {filename}")

def message_file_append(filename):
    print(f"Data successfully appended to {filename}")
    
def message_file_delete(filename):
    print(f"File {filename} successfully deleted")

def message_file_reset(filename):
    print(f"File {filename} has been reset")

# Errors
def error_format():
    print("Invalid format!")

def error_invalid_chara():
    print("Invalid characted detected!")

def error_division_zero():
    print("Can't divide by 0! (would make +∞, -∞ or 0 anyway)")

def error_saving(e):
    print(f"Error saving to file: {e}")

def error_append_file(e):
    print(f"Error appending to file: {e}")

def error_delete(e):
    print(f"Error deleting file: {e}")

def error_file_not_exist(filename):
    print(f"File {filename} does not exist")
    
def error_reset(e):
    print(f"Error resetting file: {e}")

def error_print(e):
    print(f'Error printing file : {e}')

def error_calculation():
    print("Something bad happened during calculation!")

# History
def history(content): #TODO temp variable; Need to know what History returns
    print(f'File content: {"\n" +content}')

# Result
def final_result(value): #TODO temp variable; Need to know how to print result
    print(f"= {value}")