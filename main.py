import display

def user_input():   
    while True:
        invalid = 0

        try:
            operation_field = display.input_operation()
        except ValueError:
            display.error_format()
            continue

        valid_characters = "0123546789+-*/ "
        for i in range(len(operation_field)):
            if operation_field[i] not in valid_characters:
                display.error_invalid_chara()
                invalid = 1
                break 
            else:
                continue
        if invalid == 1:
            invalid = 0
            continue
        
        numbers_temp, operators_temp = operation_field, operation_field
        for symbol in valid_characters[10:]:
            numbers_temp = numbers_temp.replace(symbol, " ")
        numbers = numbers_temp.split()
        for digit in valid_characters[:10]:
            operators_temp = operators_temp.replace(digit, " ")
        operators = operators_temp.split()

        result = float(numbers[0])
        for i in range(len(operators)):
            match operators[i]:
                case "+": result = result + float(numbers[i+1])
                case "-": result = result - float(numbers[i+1])
                case "*": result = result * float(numbers[i+1])
                case "/": 
                    try:
                        result = result / float(numbers[i+1])
                    except ZeroDivisionError:
                        display.error_division_zero()

        return result
def main():
    while True:
        final_result = user_input()
        display.result(final_result)

main()