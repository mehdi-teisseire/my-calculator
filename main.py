import history, display
from rules import resolve_math_input
import os

def clear_screen():
    #Clear the terminal screen based on operating system.
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        print("1. Calculator")
        print("2. History manager")
        menu_choice =input("Enter your Choice (1-2)")
        clear_screen()
        if menu_choice == "1":
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
                
        elif menu_choice == "2" :
            history.display_menu('history')
            clear_screen()
main()