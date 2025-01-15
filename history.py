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
    
