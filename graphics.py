import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("MyCaLcuLatoR")
        self.geometry("500x800")

        
        #Configure row/column
        for i in range(3):
            self.columnconfigure(i, weight=1)        
        self.rowconfigure(0, weight=1)
        
        #Operator buttons
        self.button_equal = customtkinter.CTkButton(self, text="=", command=self.button_callbck)
        self.button_equal.grid(row= 2, column = 4, rowspan = 2, columnspan = 2)

        self.button_plus = customtkinter.CTkButton(self, text="+", command=self.button_callbck)
        self.button_plus.grid(row= 1, column = 4)

        self.button_minus = customtkinter.CTkButton(self, text="-", command=self.button_callbck)
        self.button_minus.grid(row= 1, column = 5)        

        self.button_multiply = customtkinter.CTkButton(self, text="*", command=self.button_callbck)
        self.button_multiply.grid(row= 2, column = 4)

        self.button_divide = customtkinter.CTkButton(self, text="/", command=self.button_callbck)
        self.button_divide.grid(row= 2, column = 5)

        self.button_numbers = []
        #Numbers buttons #i%3 = 0 1 2 0 1 2 0 1 2      #i//3 = 0 0 0 1 1 1 2 2 2
        self.button_numbers.append(customtkinter.CTkButton(self, text="0", command=self.button_callbck))
        self.button_numbers[0].grid(row = 4, column = 1, sticky="ew", columnspan = 3) 
        for i in range(1, 10):
            self.button_numbers.append(customtkinter.CTkButton(self, text=i, command=self.button_callbck))
            self.button_numbers[i].grid(row = (i//3)+1, column = i%3, sticky="ew") 



        

    def button_callbck(self):
        test = self.button_numbers.cget("text")
        print(test)

app = App()
app.mainloop()

