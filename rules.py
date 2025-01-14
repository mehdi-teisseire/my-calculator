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

    # Too apply an operator on 2 values
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