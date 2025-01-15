import customtkinter

class OperatorFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #Operator buttons
        self.button_equal = customtkinter.CTkButton(self, text="=", command=self.button_display_result)
        self.button_equal.grid(row = 3, column = 4, rowspan = 2, columnspan = 2)

        self.button_plus = customtkinter.CTkButton(self, text="+", command=self.button_input_character)
        self.button_plus.grid(row = 1, column = 4)

        self.button_minus = customtkinter.CTkButton(self, text="-", command=self.button_input_character)
        self.button_minus.grid(row = 1, column = 5)        

        self.button_multiply = customtkinter.CTkButton(self, text="*", command=self.button_input_character)
        self.button_multiply.grid(row = 2, column = 4)

        self.button_divide = customtkinter.CTkButton(self, text="/", command=self.button_input_character)
        self.button_divide.grid(row = 2, column = 5)

    def button_input_character(self):
        print(self.value)
        #test = self.cget("text")
        #print(test)

    def button_display_result(self):
        print(self)

class NumbersFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.button_numbers = []

        #Numbers buttons #i%3 = 0 1 2 0 1 2 0 1 2      #i//3 = 0 0 0 1 1 1 2 2 2
        self.button_numbers.append(customtkinter.CTkButton(self, text="0", command=self.button_input_character))
        self.button_numbers[0].grid(row = 4, column = 0, columnspan = 3) 
        for i in range(1, 10):
            self.button_numbers.append(customtkinter.CTkButton(self, text=i, command=self.button_input_character))
            self.value = i
            self.button_numbers[i].grid(row = (i-1)//3, column = (i-1)%3)

    def button_input_character(self):
        print(self.value)
        #test = self.cget("text")
        #print(test)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("MyCaLcuLatoR")
        self.geometry("400x600")

        #Configure row/column
        self.columnconfigure(0, weight = 1)
        for i in range(3): self.columnconfigure(1 ,weight = 1)
        self.columnconfigure(3, weight= 2)
        for i in range(4,6): self.columnconfigure(i, weight=1)

        self.rowconfigure(0, weight = 1)
        for i in range(1,5): self.rowconfigure(1, weight = 2)
        

        #self.result_frame = ResultFrame(self)
        #self.result_frame.grid(row = 0, column = 0, sticky="nsew")

        self.operator_frame = OperatorFrame(self)
        self.operator_frame.grid(row = 1, column = 4, sticky="ns")

        self.numbers_frame = NumbersFrame(self)
        self.numbers_frame.grid(row = 1, column = 0, sticky="ns")

app = App()
app.mainloop()


    #   self.button_equal = customtkinter.CTkButton(self, text="=", command=self.button_display_result)
    #     self.button_equal.grid(row= 2, column = 4, rowspan = 2, columnspan = 2)

    #     self.button_plus = customtkinter.CTkButton(self, text="+", command=self.button_input_character)
    #     self.button_plus.grid(row= 1, column = 4)

    #     self.button_minus = customtkinter.CTkButton(self, text="-", command=self.button_input_character)
    #     self.button_minus.grid(row= 1, column = 5)        

    #     self.button_multiply = customtkinter.CTkButton(self, text="*", command=self.button_input_character)
    #     self.button_multiply.grid(row= 2, column = 4)

    #     self.button_divide = customtkinter.CTkButton(self, text="/", command=self.button_input_character)
    #     self.button_divide.grid(row= 2, column = 5)

    #     self.button_numbers = []

    #     #Numbers buttons #i%3 = 0 1 2 0 1 2 0 1 2      #i//3 = 0 0 0 1 1 1 2 2 2
    #     self.button_numbers.append(customtkinter.CTkButton(self, text="0", command=self.button_input_character))
    #     self.button_numbers[0].grid(row = 4, column = 1, columnspan = 3, sticky="ew") 
    #     for i in range(1, 10):
    #         self.button_numbers.append(customtkinter.CTkButton(self, text=i, command=self.button_input_character))
    #         self.button_numbers[i].grid(row = (i//3)+1, column = i%3, sticky="ew") 