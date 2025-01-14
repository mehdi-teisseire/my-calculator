import display
# Rules

# User input 
def user_input():   
    while True:
        try:
            operation_field = display.input_operation()
            operation_field = operation_field.replace('=', '').strip() 
            valid_characters = "0123456789+-*/()%. "
            for character in operation_field:
                if character not in valid_characters:
                    display.error_invalid_chara()
                    break
            else:
                try:
                    result = resolve_math_input(operation_field) 
                    return result  
                except ZeroDivisionError:
                    display.error_division_zero() 
                except Exception:
                    display.error_format()
        except ValueError:
            display.error_format()

#
def resolve_math_input(math_input):

    # To apply an operator on 2 values
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
            if right_value == 0:
                raise ZeroDivisionError(" HA! Division by 0! ")
            value_list.append(left_value / right_value)
        elif operator == '%':
            value_list.append(left_value % right_value)
        elif operator == '//':
            value_list.append(left_value // right_value)
        elif operator == '**':
            value_list.append(left_value ** right_value)
        elif operator == '**0.5':
            value_list.append(left_value **0.5 )

    # To rule the operation order (0= highest priority)
    def operator_priority(operator):
        if operator == '(':
            return 0  
        if operator == ')':
            return 5  
        if operator ==('** , **0.5 '):
            return 1 
        if operator in ('*', '/', '%', '//'):
            return 3  
        if operator in ('+', '-'):
            return 4  
        return -1 
    
    operator_list = []
    value_list = []
    index = 0
    # Check for white space and skip
    while index < len(math_input):
        if math_input[index] == ' ':
            index += 1
            continue
        # Check for numbers and negative signs
        if math_input[index].isdigit() or (math_input[index] == '-' and (index == 0 or math_input[index-1] in '*/-()')):
            number_str = ''
            is_negative = (math_input[index] == '-')
            if is_negative:
                index +=1
            # Build number string handleling digits or decimal point
            while (index < len(math_input) and (math_input[index].isdigit() or math_input[index] == '.')):
                number_str += math_input[index]
                index += 1
            number = float(number_str)
            if is_negative:
                number = -number
            value_list.append(number)
            continue
        # Handle () opening and closing   
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
    # Add remaining operators in the list
    while operator_list:
        apply_operator(operator_list, value_list)

    return value_list[0] 