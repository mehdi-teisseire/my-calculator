import rules, history
import customtkinter

class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        
        # input that accept direct keys or buttons
        # display result in input directly or in label next to it (weight 4:1)

        #CTkEntry -> see webpage

class NumbersFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        for i in range(3): 
            self.columnconfigure(i ,weight = 1)

        for i in range(5):
            self.rowconfigure(i, weight = 1)

        self.button_numbers = []

        #Numbers buttons #i%3 = 0 1 2 0 1 2 0 1 2      #i//3 = 0 0 0 1 1 1 2 2 2
        self.button_open_bracket = customtkinter.CTkButton(self, text="(", font=master.fonts, command=lambda: master.input_operation.insert('end', "("))
        self.button_open_bracket.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "news") 

        self.button_close_bracket = customtkinter.CTkButton(self, text=")", font=master.fonts, command=lambda: master.input_operation.insert('end', ")"))
        self.button_close_bracket.grid(row = 0, column = 1, padx = 2, pady = 2, sticky = "news") 

        self.button_memory = customtkinter.CTkButton(self, text="DEL", font=master.fonts, command=lambda: master.input_operation.delete(int(len(master.input_operation.get())-1), 'end')) #replace with last value
        self.button_memory.grid(row = 0, column = 2, padx = 2, pady = 2, sticky = "news") 

        self.button_numbers.append(customtkinter.CTkButton(self, text="0", font=master.fonts, command=lambda: self.button_input_character(master, "0")))
        self.button_numbers[0].grid(row=4, column=0, columnspan=2, padx=2, pady=2, sticky="news")

        for i in range(1, 10):
            self.button_numbers.append(customtkinter.CTkButton(self, text=i, font=master.fonts, command=lambda i=i: self.button_input_character(master, str(i))))
            self.button_numbers[i].grid(row=((i-1)//3)+1, column=(i-1)%3, padx=2, pady=2, sticky="news")

        self.button_numbers.append(customtkinter.CTkButton(self, text=".", font=master.fonts, command=lambda: self.button_input_character(".")))
        self.button_numbers[10].grid(row=4, column=2, padx=2, pady=2, sticky="news")

    def button_input_character(self, master, text):
        if master.flag_clear == True:
            master.input_operation.delete(0, len(master.input_operation.get()))
            master.flag_clear = False

        current_text = self.master.input_operation.get()
        new_text = current_text + text
        self.master.input_operation.delete(0, customtkinter.END) 
        self.master.input_operation.insert(0, new_text) 

        
class OperatorFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Columns in frame Operator
        for i in range(2): 
            self.columnconfigure(i ,weight = 1)
            
        # Rows in frame Operator
        for i in range(5):
            self.rowconfigure(i, weight = 1)
        

        # Operator buttons

        self.button_memory = customtkinter.CTkButton(self, text="C", font=master.fonts, command=lambda: master.input_operation.delete(0, len(master.input_operation.get()))) #replace with last value
        self.button_memory.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "news") 

        self.button_exponent = customtkinter.CTkButton(self, text="**", font=master.fonts, command=lambda: master.input_operation.insert('end', "**"))
        self.button_exponent.grid(row = 0, column = 1, padx= 2, pady = 2, sticky = "news")

        self.button_plus = customtkinter.CTkButton(self, text="+", font=master.fonts, command=lambda: master.input_operation.insert('end', "+"))
        self.button_plus.grid(row = 1, column = 0, padx= 2, pady = 2, sticky = "news")
       
        self.button_minus = customtkinter.CTkButton(self, text="-", font=master.fonts, command=lambda: master.input_operation.insert('end', "-"))
        self.button_minus.grid(row = 1, column = 1, padx= 2, pady = 2, sticky = "news")
        
        self.button_multiply = customtkinter.CTkButton(self, text="*", font=master.fonts, command=lambda: master.input_operation.insert('end', "*"))
        self.button_multiply.grid(row = 2, column = 0, padx= 2, pady = 2, sticky = "news")
        
        self.button_divide = customtkinter.CTkButton(self, text="/", font=master.fonts, command=lambda: master.input_operation.insert('end', "/"))
        self.button_divide.grid(row = 2, column = 1, padx= 2, pady = 2, sticky = "news")
        
        self.button_divide = customtkinter.CTkButton(self, text="%", font=master.fonts, command=lambda: master.input_operation.insert('end', "%"))
        self.button_divide.grid(row = 3, column = 0, padx= 2, pady = 2, sticky = "news")

        self.button_divide = customtkinter.CTkButton(self, text="//", font=master.fonts, command=lambda: master.input_operation.insert('end', "//"))
        self.button_divide.grid(row = 3, column = 1, padx= 2, pady = 2, sticky = "news")

        self.button_equal = customtkinter.CTkButton(self, text="=", font=master.fonts, command=lambda: self.button_display_result(master)) # replace with result
        self.button_equal.grid(row = 4, column = 0, columnspan = 2, padx = 2, pady = 20, sticky = "news")
        #self.button_equal.bind('<Return>', master.input_operation.insert(0, '<Return>'))

    def button_display_result(self, master):
        operation_input = master.input_operation.get() 
        result = rules.user_input(operation_input)  
        if result is not None:
            final_result = rules.resolve_math_input(result)  
            master.input_operation.delete(0, customtkinter.END) 
            master.input_operation.insert(0, final_result) 
            self.print_file("history.txt")
            master.flag_clear = True

    def handle_terminal_input(self):
        operation_input = rules.user_input_terminal() 
        if operation_input:
            final_result = rules.resolve_math_input(operation_input)
            print(f"Résultat : {final_result}")

    def print_file(filename, master):
            # if not filename.endswith('.txt'):
            #     filename += '.txt'
            try:
                with open(filename,'r') as file :
                    content = file.read()
                    master.history_window.text_file.delete(0,'end')
                    master.history_window.text_file.insert(0, history(content))
                    print(content)
                    #self.configfile.insert(0, history(content))
            except Exception as e:
                pass


class HistoryWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__()
        self.title("History")
        self.geometry("300x600")

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        text_file = customtkinter.CTkTextbox(self, state = "disabled")
        text_file.grid(row = 0, column = 0, sticky = "news")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("MyCaLcuLatoR")
        self.geometry("500x600")
        customtkinter.set_default_color_theme("./custom_theme.json")

        # Configure row/column
        self.columnconfigure(0, weight= 2)
        self.columnconfigure(1, weight= 2)

        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 2)

        self.fonts = customtkinter.CTkFont(family = 'Arial', size = 30)

        self.flag_clear = False

        # Input 
        self.input_operation = customtkinter.CTkEntry(self, font=self.fonts, placeholder_text="type something")
        self.input_operation.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 15, sticky = "news")

        # Frames
        self.numbers_frame = NumbersFrame(self)
        self.numbers_frame.grid(row = 1, column = 0, sticky="news")

        self.operator_frame = OperatorFrame(self)
        self.operator_frame.grid(row = 1, column = 1, sticky="news")

        # History
        self.history_window = HistoryWindow(self)

app = App()
app.mainloop()