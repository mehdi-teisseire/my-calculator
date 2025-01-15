import history
def main():
  while True:

        invalid = False
        operation_input = user_input()
        chr_string = valid_chr(operation_input)
        if invalid == True:
            continue
        final_result=calculator(chr_string,operation_input)
        print(final_result)
        history.new_history(final_result,)

        while True:
            graphic_type = display.input_graphics_type()
            if graphic_type = True:
                else:
                    user_str = display.input_operation()
            #history.open()
            final_result = resolve_math_input(user_str)
            display.final_result(final_result)


main()