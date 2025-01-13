# Rules

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

    # To rule the operation order (0= highest priority)
    def operator_priority(operator):
        if operator == '(':
            return 0
        if operator == ')':
            return 4
        if operator in ('+', '-'):
            return 1
        if operator in ('*', '/'):
            return 2
        return -1
    
    operator_list = []
    value_list = []
    index = 0

    while index < len(math_input):
        if math_input[index] == ' ':
            index += 1
            continue


