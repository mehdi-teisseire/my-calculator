import graphics
import history, display
from rules import resolve_math_input


def graphic_choice():
    graph = display.input_graphic_selection()
    if graph == True:
        main2()
    else:
        main()
def main2():
    graphics.app.mainloop()

def main():
    while True:
        #while True
            #graphic_type = display.input_graphics_type()
        #if graphic_type = True:
        #else:
        
            history.print_file("history")
            final_result = 0                                                              # History is read and displayed
            operation_field = display.input_operation()                                                 # User operation input
            try:
                operation_field = operation_field.replace('=', '').strip()
                operation_field = operation_field.replace(" ", "") 
                valid_characters = [
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
                    "+", "-", "*", "/", "(", ")", "%", " ", "//", "**", "."
                ]
                for character in operation_field:
                    if character not in valid_characters:
                        display.error_invalid_chara()
                        break
                else:                                         
                    try:
                        final_result = resolve_math_input(operation_field)                              # Result is calculated
                          
                    except ZeroDivisionError:
                        display.error_division_zero()
                        continue
                    except Exception:
                        display.error_calculation()
                        continue
    
                    display.final_result(final_result)                                                  # Result is displayed
                    history.append_to_file(operation_field + " = " + str(final_result), "history")      # Whole operation + result is added to file

            except ValueError:
                display.error_format()

graphic_choice()