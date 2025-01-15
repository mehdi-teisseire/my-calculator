import customtkinter

class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.rowconfigure(0)
        self.columnconfigure(0)

        # input that accept direct keys or buttons
        # display result in input directly or in label next to it (weight 4:1)

        


class NumbersFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        for i in range(3): 
            self.columnconfigure(i ,weight = 1)

        for i in range(4):
            self.rowconfigure(i, weight = 1)

        self.button_numbers = []

        #Numbers buttons #i%3 = 0 1 2 0 1 2 0 1 2      #i//3 = 0 0 0 1 1 1 2 2 2
        self.button_numbers.append(customtkinter.CTkButton(self, text="0", command=self.button_input_character))
        self.button_numbers[0].grid(row = 3, column = 0, columnspan = 2, padx = 2, pady = 2, sticky = "news") 

        for i in range(1, 10):
            self.button_numbers.append(customtkinter.CTkButton(self, text=i, command=self.button_input_character))
            self.value = i
            self.button_numbers[i].grid(row = (i-1)//3, column = (i-1)%3, padx = 2, pady = 2, sticky = "news")

        self.button_numbers.append(customtkinter.CTkButton(self, text=".", command=self.button_input_character))
        self.button_numbers[10].grid(row = 3, column = 2, padx = 2, pady = 2, sticky = "news") 

    def button_input_character(self):
        print(self.value)
        #test = self.cget("text")
        #print(test)

class OperatorFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Columns in frame Operator
        for i in range(2): 
            self.columnconfigure(i ,weight = 1)
            
        # Rows in frame Operator
        for i in range(2):
            self.rowconfigure(i, weight = 1)
        self.rowconfigure(2, weight = 2)

        # Operator buttons
        self.button_plus = customtkinter.CTkButton(self, text="+", command=self.button_input_character)
        self.button_plus.grid(row = 0, column = 0, padx= 2, pady = 2, sticky = "news")

        self.button_minus = customtkinter.CTkButton(self, text="-", command=self.button_input_character)
        self.button_minus.grid(row = 0, column = 1, padx= 2, pady = 2, sticky = "news")

        self.button_multiply = customtkinter.CTkButton(self, text="*", command=self.button_input_character)
        self.button_multiply.grid(row = 1, column = 0, padx= 2, pady = 2, sticky = "news")

        self.button_divide = customtkinter.CTkButton(self, text="/", command=self.button_input_character)
        self.button_divide.grid(row = 1, column = 1, padx= 2, pady = 2, sticky = "news")
        
        self.button_equal = customtkinter.CTkButton(self, text="=", command=self.button_display_result)
        self.button_equal.grid(row = 2, column = 0, columnspan = 2, padx = 2, pady = 20, sticky = "news")

    def button_input_character(self):
        print(self.value)
        #test = self.cget("text")
        #print(test)

    def button_display_result(self):
        print(self)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("MyCaLcuLatoR")
        self.geometry("500x600")

        # Configure row/column
        self.columnconfigure(0, weight= 2)
        self.columnconfigure(1, weight= 2)

        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 2)

        # Frames
        self.input_frame = InputFrame(self)
        self.operator_frame.grid(row = 0, column = 0, columnspan= 2, sticky="ns")

        self.numbers_frame = NumbersFrame(self)
        self.numbers_frame.grid(row = 1, column = 0, sticky="news")

            #maybe a separator here?

        self.operator_frame = OperatorFrame(self)
        self.operator_frame.grid(row = 1, column = 1, sticky="news")

            #history on a new window
        #self.history_frame = HistoryFrame(self)
        #self.operator_frame.grid

app = App()
app.mainloop()
