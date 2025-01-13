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

    # To rule the operation order (1= low priority)
    def operator_priority(operator):
        if operator in ('+', '-'):
            return 1
        if operator in ('*', '/'):
            return 2
        return 0
    
    operator_list = []
    value_list = []
    index = 0
    


