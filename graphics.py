#import rules
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

        self.button_numbers.append(customtkinter.CTkButton(self, text="0", font=master.fonts, command=lambda: master.input_operation.insert('end', "0")))
        self.button_numbers[0].grid(row = 4, column = 0, columnspan = 2, padx = 2, pady = 2, sticky = "news") 

        self.button_numbers.append(customtkinter.CTkButton(self, text="1", font=master.fonts, command=lambda: master.input_operation.insert('end', "1")))
        self.button_numbers[1].grid(row = 1, column = 0, padx = 2, pady = 2, sticky = "news") 

        self.button_numbers.append(customtkinter.CTkButton(self, text="2", font=master.fonts, command=lambda: master.input_operation.insert('end', "2")))
        self.button_numbers[2].grid(row = 1, column = 1, padx = 2, pady = 2, sticky = "news") 

        self.button_numbers.append(customtkinter.CTkButton(self, text="3", font=master.fonts, command=lambda: master.input_operation.insert('end', "3")))
        self.button_numbers[3].grid(row = 1, column = 2, padx = 2, pady = 2, sticky = "news") 

        self.button_numbers.append(customtkinter.CTkButton(self, text="4", font=master.fonts, command=lambda: master.input_operation.insert('end', "4")))
        self.button_numbers[4].grid(row = 2, column = 0, padx = 2, pady = 2, sticky = "news") 

        self.button_numbers.append(customtkinter.CTkButton(self, text="5", font=master.fonts, command=lambda: master.input_operation.insert('end', "5")))
        self.button_numbers[5].grid(row = 2, column = 1, padx = 2, pady = 2, sticky = "news") 

        self.button_numbers.append(customtkinter.CTkButton(self, text="6", font=master.fonts, command=lambda: master.input_operation.insert('end', "6")))
        self.button_numbers[6].grid(row = 2, column = 2, padx = 2, pady = 2, sticky = "news") 

        self.button_numbers.append(customtkinter.CTkButton(self, text="7", font=master.fonts, command=lambda: master.input_operation.insert('end', "7")))
        self.button_numbers[7].grid(row = 3, column = 0, padx = 2, pady = 2, sticky = "news") 

        self.button_numbers.append(customtkinter.CTkButton(self, text="8", font=master.fonts, command=lambda: master.input_operation.insert('end', "8")))
        self.button_numbers[8].grid(row = 3, column = 1, padx = 2, pady = 2, sticky = "news") 

        self.button_numbers.append(customtkinter.CTkButton(self, text="9", font=master.fonts, command=lambda: master.input_operation.insert('end', "9")))
        self.button_numbers[9].grid(row = 3, column = 2, padx = 2, pady = 2, sticky = "news") 

        self.button_dot = customtkinter.CTkButton(self, text=".", font=master.fonts, command=lambda: master.input_operation.insert('end', "."))
        self.button_dot.grid(row = 4, column = 2, padx = 2, pady = 2, sticky = "news") 

    def button_input_character(self):
        pass
        # result = rules.user_input(.input_operation.get())
        #test = self.cget("text")
        #print(test)

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

    def handle_terminal_input(self):
        operation_input = rules.user_input_terminal() 
        if operation_input:
            final_result = rules.resolve_math_input(operation_input)
            print(f"Résultat : {final_result}")


class HistoryWindow(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__()
        self.title("History")
        self.geometry("300x600")

        print('selected:', history.txt )

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