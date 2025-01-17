import display

# graphic user input
def user_input(operation_field):
    operation_field = operation_field.replace('=', '').strip()
    operation_field = operation_field.replace(" ", "")
    
    valid_characters = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
        "+", "-", "*", "/", "(", ")", "%", " ", "//", "**", "."
    ]
    
    for character in operation_field:
        if character not in valid_characters:
            display.error_invalid_chara()
            return None 
    
    return operation_field

# terminal user input
def user_input_terminal():
    operation_field = display.input_operation() 
    operation_field = operation_field.replace('=', '').strip()
    operation_field = operation_field.replace(" ", "")
    
    valid_characters = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
        "+", "-", "*", "/", "(", ")", "%", " ", "//", "**", "."
    ]
    
    for character in operation_field:
        if character not in valid_characters:
            display.error_invalid_chara()
            return None 
    
    return operation_field

    # Simplify consecutive operators
def simplify_consecutive_operators(expression):
    expression = expression.replace("+-", "-")
    expression = expression.replace("-+", "-")
    expression = expression.replace("--", "+")
    expression = expression.replace("++", "+")
    return expression

    # Apply an operator on 2 values
def apply_operator(operator_list, value_list):
    right_value = value_list.pop()
    left_value = value_list.pop()
    operator = operator_list.pop()

    if operator == '+':
        value_list.append(left_value + right_value)
    elif operator == '-':
        value_list.append(left_value - right_value)
    elif operator == '*':
        value_list.append(left_value * right_value)
    elif operator == '/':
        value_list.append(left_value / right_value)
    elif operator == '%':
        value_list.append(left_value % right_value)
    elif operator == '//':
        value_list.append(left_value // right_value)
    elif operator == '**':
        value_list.append(left_value ** right_value)

# To rule the operation order (0= highest priority)
def operator_priority(operator):
    if operator == '(':
        return 0  
    if operator == ')':
        return 5  
    if operator == '**':
        return 4 
    if operator in ('*', '/', '%', '//'):
        return 3  
    if operator in ('+', '-'):
        return 2  
    return -1 

# main function that resolve the inputed operation
def resolve_math_input(math_input):
 
    operator_list = []
    value_list = []
    index = 0
    
    # Simplify the input expression before processing
    math_input = simplify_consecutive_operators(math_input)

    while index < len(math_input):
        if math_input[index] == ' ':
            index += 1
            continue
        
        # Check for numbers (including negative numbers)
        if math_input[index].isdigit() or (math_input[index] == '-' and (index == 0 or math_input[index-1] in '*/-()')):
            number_str = ''
            is_negative = (math_input[index] == '-')
            if is_negative:
                index += 1
            
            # Build the number string handling digits or decimal point
            while (index < len(math_input) and (math_input[index].isdigit() or math_input[index] == '.')):
                number_str += math_input[index]
                index += 1
            
            number = float(number_str)
            if is_negative:
                number = -number
            value_list.append(number)
            continue
        
        # Handle multi-character operators
        if math_input[index:index+2] in ['//', '**']:
            operator_list.append(math_input[index:index+2])
            index += 2
            continue
        
        # Handle parentheses
        if math_input[index] == '(':
            operator_list.append(math_input[index])  
        elif math_input[index] == ')':
            while operator_list and operator_list[-1] != '(':
                apply_operator(operator_list, value_list)
            operator_list.pop() 
        else:
            # Handle operator priority
            while (operator_list and operator_priority(operator_list[-1]) >= operator_priority(math_input[index])):
                apply_operator(operator_list, value_list)
            operator_list.append(math_input[index])  
        
        index += 1
    
    # Apply remaining operators in the list
    while operator_list:
        apply_operator(operator_list, value_list)

    return value_list[0]