def user_input():   
    while True:
        try:
            operation_field = input("Calculate something:\n")
        except ValueError:
            print("Invalid format")
        valid_characters = "0123546789+-*/ "
        for i in range(len(operation_field)):
            if operation_field[i] not in valid_characters:
                print("No.")
                break 
            else:
                continue
        
        numbers_temp, operators_temp = operation_field, operation_field
        for symbol in valid_characters[10:]:
            numbers_temp = numbers_temp.replace(symbol, " ")
        numbers = numbers_temp.split()
        for digit in valid_characters[:10]:
            operators_temp = operators_temp.replace(digit, " ") #.strip()
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
                        print("Ha!")

        return result

final_result = user_input()
print(final_result)

