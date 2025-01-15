def save_to_file(data, filename):

    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename, 'w') as file:
            file.write(str(data))
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def append_to_file(data, filename):
    
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename, 'a') as file:
            file.write(str(data) + '\n')
        print(f"Data successfully appended to {filename}")
    except Exception as e:
        print(f"Error appending to file: {e}")

def delete_file(filename):
    
    import os
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File {filename} successfully deleted")
        else:
            print(f"File {filename} does not exist")
    except Exception as e:
        print(f"Error deleting file: {e}")

def reset_file(filename):

    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename, 'w') as file:
            file.write('') 
        print(f"File {filename} has been reset")
    except Exception as e:
        print(f"Error resetting file: {e}")

def print_file(filename):

    if not filename.endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename,'r') as file :
            content = file.read()
            print(f'File content: {"\n" +content}')
    except Exception as e:
        print(f'Error printing file : {e}')
    
