import display

def save_to_file(data, filename):

    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename, 'w') as file:
            file.write(str(data))
        display.message_file_open(filename)
    except Exception as e:
        display.error_saving(e)

def append_to_file(data, filename):
    
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename, 'a') as file:
            file.write(str(data) + '\n')
        display.message_file_open(filename)
    except Exception as e:
        display.error_append_file(e)
def delete_file(filename):
    
    import os
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        if os.path.exists(filename):
            os.remove(filename)
            display.message_file_delete(filename)
        else:
            display.error_file_not_exist(filename)
    except Exception as e:
        display.error_delete(e)

def reset_file(filename):

    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename, 'w') as file:
            file.write('') 
        display.message_file_reset(filename)
    except Exception as e:
        display.error_reset(e)

def print_file(filename):

    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename,'r') as file :
            content = file.read()
            display.history(content)
    except Exception as e:
        display.error_print(e)

def display_menu(filename):
    while True:
        print("\n=== File Operations Menu ===")
        print("1. Show history")
        print("2. Reset/clear file")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
        
        if choice == "1":
            print_file(filename)
                
        elif choice == '2':
            confirmation = input(f"Are you sure you want to reset {filename}.txt? (yes/no): ")
            if confirmation.lower() == 'yes':
                reset_file(filename)
            else:
                print("Reset cancelled")
                
        else:
            print("Invalid choice! Please enter a number between 1 and 4")
        
        input("\nPress Enter to continue...")
