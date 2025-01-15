import history, display
from rules import user_input

def main():
    while True:
        #while True
            #graphic_type = display.input_graphics_type()
        #if graphic_type = True:
        #else:
            user_str = display.input_operation()
            history.print_file()
            final_result = user_input()
            display.final_result(final_result)

main()